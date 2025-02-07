# config_pearl

The [main](https://github.com/uasal/config_pearl/tree/main) branch of this repo is under STP change control. The [develop](https://github.com/uasal/config_pearl/tree/develop) branch is currently the default to enable rapid development of systems engineering budgets but the default will be changed to main once baseline observatory design is frozen. Changes to main require code owner approval, changes to the develop branch require approval of two other team members.

Details on the change control process are found in the [coronograph design documentation repository](https://github.com/uasal/spacecoron_design_docs)

This repository contains reference data for the observatory and telescope.
The data in the repository is mean to encapsulate all parameters which represent the high-level system and are to be identical when called by the the various tools/simulators.
This includes things like information about the telescope optical system, such as coatings and sensors, and observatory properties such as slew times.
A synthetic dataset regarding the timeseries for the wavefront error due the thermal effects is also available.

The parameters for each subsystem are found in the `config` directory.
A description of how configurations are used in UASAL software, users can find an example notebook in the `docs` directory of the  [config_project_template](https://github.com/uasal/config_project_template) repository. 
The example demonstrates how to load the TOML parameter files in a Python script.
TOML files are human readible configuration files that can be read with a range of parsers https://github.com/toml-lang/toml/wiki

## Git large file storage (LFS)

This repository makes use of the git large file storage for files listed in the `.gitattributes` file.
Accessing these files will require users having (Git Large File Storage (LFS))[https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage] installed on their local machine.

If you have Git LFS installed, then the large files will be pulled by default.
This can be disabled in your gitconfig, as described (at this link)[https://stackoverflow.com/questions/42019529/how-to-clone-pull-a-git-repository-ignoring-lfs].