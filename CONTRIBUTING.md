# Guide to Contributing

## Please see [developer guide](https://garnet-neutrons.org.readthedocs.build/en/latest/Developer/index.html) for full contributing guidelines

Contributions to this project are welcome. All contributors agree to the following:
- You have permission and any required rights to submit your contribution.
- Your contribution is provided under the license of this project and may be redistributed as such.
- All contributions to this project are public.

All contributions must be ["signed off"](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) in the commit
log and by doing so you agree to the above.


## Quick start for developers

Clone the repository and setup the environment

```bash
git clone git@github.com:neutrons/garnet.git
cd garnet
conda env create -f environment.yml
conda activate <garnet-environment>
pip install -e .
```

After following these instructions, you can run Garnet from the project root directory as:

```bash
garnet
```

To run Garnet tests from the project root directory:

```bash
python -m pytest
```
