"""Build the manual and API reference, then check local links."""
from pathlib import Path
import os, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
env=dict(os.environ,NO_MKDOCS_2_WARNING='1')
subprocess.run([sys.executable,'-m','mkdocs','build','--strict'],cwd=ROOT,env=env,check=True)
docfx=shutil.which('docfx') or str(Path.home()/'.dotnet/tools/docfx.exe')
subprocess.run([docfx,'build','docfx/docfx.json','--warningsAsErrors','--disableGitFeatures'],cwd=ROOT,check=True)
subprocess.run([sys.executable,'scripts/check_content.py'],cwd=ROOT,check=True)
