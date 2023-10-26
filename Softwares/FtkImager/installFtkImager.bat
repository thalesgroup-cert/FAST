for %%f in (*.exe) do (
    if "%%~xf"==".exe" %%f /S /v/qn
)