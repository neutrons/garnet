## Description of Changes:
<!-- Add a description here-->


## Related Items
<!-- Links to related issues or pull requests -->
<!-- Links to IBM EWM items if aplicable -->

## To Test:

<!-- Instructions for testing.
There should be sufficient instructions for someone unfamiliar with the application to test.
If you have created a manual test, provide the code here as well.
You can provide a manual test in a code block using:
```python
# some python code
```
-->

```bash
cd /path/to/my/local/garnet/repo/
git fetch origin merge-requests/<MERGE_REQUEST_NUMBER>/head:mr<MERGE_REQUEST_NUMBER>
git switch mr<MERGE_REQUEST_NUMBER>
conda activate <garnet_environment>
python -m pytest <item_to_test>
```
<!--
In the above code snippet, substitute `<MERGE_REQUEST_NUMBER>` for the actual merge request number. Also substitute
`<garnet_environment>` with the name of the conda environment you use for development. It is critical that
you have installed the repo in this conda environment in editable mode with `pip install -e .` or `conda develop .`
Substitute `<item_to_test>` with the path to the file or directory of your test. If you have multiple tests in multiple locations, please list them.
-->

## Check list for the pull request
- [ ] I have read the [CONTRIBUTING]
- [ ] I have read the [CODE_OF_CONDUCT]
- [ ] I have added tests for my changes
- [ ] I have updated the documentation accordingly

---

## Check list for the reviewer
- [ ] I have read the [CONTRIBUTING]
- [ ] I have verified the proposed changes
- [ ] best software practices
    + [ ] all internal functions have an underbar, as is python standard
    + [ ] clearly named variables (better to be verbose in variable names)
    + [ ] code comments explaining the intent of code blocks
- [ ] All the tests are passing
- [ ] The documentation is up to date
- [ ] code comments added when explaining intent
