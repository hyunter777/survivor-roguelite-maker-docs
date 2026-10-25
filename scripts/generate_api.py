"""Generate public API metadata from a locally installed package. Product source stays local."""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse, json, os, re, shutil, subprocess
import yaml

class DocfxLoader(yaml.CSafeLoader):
    pass
DocfxLoader.add_constructor('tag:yaml.org,2002:value', lambda loader, node: loader.construct_scalar(node))

ROOT = Path(__file__).resolve().parents[1]
PARTS = {
    'Core': ('Runtime/Core', []),
    'Simulation': ('Runtime/Simulation', ['Core']),
    'Run': ('Runtime/Run', ['Core', 'Simulation']),
    'Balance': ('Runtime/Balance', ['Core', 'Simulation', 'Run']),
    'Data': ('Runtime/Data', ['Core', 'Simulation', 'Run']),
    'Presentation': ('Runtime/Presentation', ['Core', 'Simulation', 'Run', 'Data']),
    'Editor': ('Editor', ['Core', 'Simulation', 'Run', 'Balance', 'Data', 'Presentation']),
}

def run(args):
    subprocess.run([str(a) for a in args], check=True, cwd=ROOT)

def clean(value):
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items() if k not in {'source', 'sourceLink', 'documentation', 'remote', 'git'} }
    if isinstance(value, list):
        return [clean(v) for v in value]
    if not isinstance(value, str): return value
    # Remove build paths and development annotations from public XML prose.
    value = re.sub(r'(?<![A-Za-z])[A-Za-z]:[\\/][^\s<>"\']+', '', value)
    value = re.sub(r'\b(?:M\d+(?:\.\d+)?|WP\d+(?:-\w+)?)\b', '', value)
    value = value.replace('should work in co-op', 'operate on additional players')
    return value

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-root', type=Path, required=True)
    parser.add_argument('--unity-managed', type=Path, required=True, help='Unity Editor Data/Managed/UnityEngine folder')
    parser.add_argument('--script-assemblies', type=Path, required=True, help='Imported project Library/ScriptAssemblies folder')
    parser.add_argument('--docfx', default=shutil.which('docfx') or str(Path.home()/'.dotnet/tools/docfx.exe'))
    args = parser.parse_args()
    package = args.package_root.resolve()
    if not (package/'package.json').is_file(): raise SystemExit('Choose the installed package root containing package.json.')
    work = ROOT/'.build/api'; work.mkdir(parents=True, exist_ok=True)
    for name,(folder,refs) in PARTS.items():
        target = work/name; target.mkdir(exist_ok=True)
        references = ''.join(f'<ProjectReference Include="../{r}/{r}.csproj" />' for r in refs)
        if name in {'Data','Presentation','Editor'}:
            references += f'<Reference Include="{escape(str(args.unity_managed.resolve()))}/*.dll" Private="false" />'
            for dll in ['UnityEngine.UI','UnityEditor.UI','Unity.TextMeshPro','Unity.InputSystem']:
                references += f'<Reference Include="{escape(str(args.script_assemblies.resolve()/dll))}.dll" Private="false" />'
        project = f'''<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup>
<TargetFramework>netstandard2.1</TargetFramework><LangVersion>9.0</LangVersion><Nullable>disable</Nullable>
<AssemblyName>SurvivorsMaker.{name}</AssemblyName><EnableDefaultCompileItems>false</EnableDefaultCompileItems>
<GenerateDocumentationFile>true</GenerateDocumentationFile><DebugType>none</DebugType>
<NoWarn>1591;0649;0169;0414</NoWarn><DefineConstants>UNITY_EDITOR;UNITY_6000_0_OR_NEWER;UNITY_2021_3_OR_NEWER</DefineConstants>
</PropertyGroup><ItemGroup><Compile Include="{escape(str(package/folder))}/**/*.cs" /></ItemGroup>
<ItemGroup>{references}</ItemGroup></Project>'''
        (target/(name+'.csproj')).write_text(project,encoding='utf-8')
    run(['dotnet','build',work/'Editor/Editor.csproj','-c','Release','--nologo'])
    binaries = work/'binaries'; binaries.mkdir(exist_ok=True)
    for name in PARTS:
        for suffix in ['dll','xml']:
            shutil.copy2(work/name/'bin/Release/netstandard2.1'/f'SurvivorsMaker.{name}.{suffix}',binaries)
    reference_dir = work/'references'; reference_dir.mkdir(exist_ok=True)
    for reference in list(args.unity_managed.glob('*.dll')) + list(args.unity_managed.parent.glob('*.dll')) + [args.script_assemblies/(n+'.dll') for n in ['UnityEngine.UI','UnityEditor.UI','Unity.TextMeshPro','Unity.InputSystem']]:
        shutil.copy2(reference, reference_dir/reference.name)
    config = {'metadata':[{'src':[{'src':binaries.as_posix(),'files':['SurvivorsMaker.*.dll']}],
        'references':['references/*.dll'],
        'dest':(ROOT/'api-metadata').as_posix(),'disableGitFeatures':True,'includePrivateMembers':False}]}
    metadata_config=work/'metadata.json'; metadata_config.write_text(json.dumps(config,indent=2),encoding='utf-8')
    run([args.docfx,'metadata',metadata_config])
    for path in (ROOT/'api-metadata').glob('*.yml'):
        text=path.read_text(encoding='utf-8-sig'); marker=text.splitlines()[0] if text.startswith('###') else ''
        data=clean(yaml.load(text,Loader=DocfxLoader))
        path.write_text((marker+'\n' if marker else '')+yaml.dump(data,Dumper=yaml.CSafeDumper,sort_keys=False,allow_unicode=True,width=120),encoding='utf-8')
    manifest={'package_version':json.loads((package/'package.json').read_text(encoding='utf-8-sig'))['version'],
        'assemblies':['SurvivorsMaker.'+part for part in PARTS], 'visibility':'public',
        'metadata_files':len(list((ROOT/'api-metadata').glob('*.yml')))}
    (ROOT/'api-metadata/manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps(manifest))

if __name__=='__main__': main()
