print("Loading libraries...")
import importlib.util, os, sys, traceback, tarfile, progressbar, pyinputplus, urllib.request, requests, zipfile, yaml

print(f"Running python: \033[1m{sys.version}\033[0m")
print("Loading modules...")

startingdir = os.getcwd()
modules = {}
cmds = {}

# Ensure directories exist
for directory in ["./modules", "./modules/_cache", "./modules/config", "./config"]:
    if not os.path.exists(directory):
        print(f"Warning: Folder {directory} was not found. Creating folder...")
        os.makedirs(directory)



# List directories in ./modules
indir = os.listdir("./modules")
if "_cache" in indir:
    indir.remove("_cache")
if "config" in indir:
    indir.remove("config")

def installpypi_module(package,version=None):
    requests.get(f"https://pypi.org/pypi/{modu}/json").json

for module_name in indir:
    module_path = os.path.join("./modules", module_name)
    if ".tar.gz" in module_name:
        print(f"Loading {module_name}")
        try:
            cache_folder = f"./modules/_cache/{module_name.split('.')[0]}"
            if not os.path.exists(cache_folder):
                print(f"Extracting {module_name} into {cache_folder}")
                with tarfile.open(os.path.join("./modules", module_name), mode="r:gz") as tar:
                    tar.extractall(path="./modules/_cache/")
            else:
                print(f"\033[33m\033[1m[WARNING]\033[33m {module_name.split('.')[0]} already exists.\nIf you are installing a newer version of the module remove the {module_name.split('.')[0]} folder in the ./modules/_cache folder")
            
            init_file = os.path.join(cache_folder, "__init__.py")
            spec = importlib.util.spec_from_file_location(module_name, init_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            modules[module_name] = module
            output = module._sch_exec()  # This is where the module sends all the info that is sent into the SCH
            cmds[output["cmd"]] = output["cmd_handler"]
        except Exception:
            print(f"\033[5m\033[1m\033[91m[ERROR]\033[0m\033[91m The module {module_name} failed to load:\n")
            traceback.print_exc()
            print("\033[0m", end="")
        else:
            print(f"\033[92mSuccessfully loaded {module_name}\033[0m")
