"""Extract complete C# examples and compile against locally prepared API assemblies."""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse, hashlib, re, subprocess
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--unity-managed',type=Path,required=True)
args=parser.parse_args()
out=ROOT/'.build/examples';out.mkdir(parents=True,exist_ok=True)
seen=set();count=0
for path in sorted((ROOT/'docs/en').rglob('*.md')):
    for code in re.findall(r'```csharp\s*\n(.*?)```',path.read_text(encoding='utf-8'),re.S):
        digest=hashlib.sha256(code.encode()).hexdigest()
        if digest in seen:continue
        seen.add(digest);count+=1;(out/f'Example{count:02}.cs').write_text(code,encoding='utf-8')
project=f'''<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>netstandard2.1</TargetFramework><LangVersion>9.0</LangVersion><Nullable>disable</Nullable></PropertyGroup><ItemGroup><ProjectReference Include="../api/Editor/Editor.csproj"/><Reference Include="{escape(str(args.unity_managed.resolve()))}/*.dll" Private="false"/></ItemGroup></Project>'''
(out/'Examples.csproj').write_text(project,encoding='utf-8')
subprocess.run(['dotnet','build',out/'Examples.csproj','--nologo'],cwd=ROOT,check=True)
print(f'Complete unique examples compiled: {count}')
