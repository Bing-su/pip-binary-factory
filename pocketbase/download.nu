let ver = open pyproject.toml | get project.version
let url = $"https://raw.githubusercontent.com/pocketbase/pocketbase/v($ver)/examples/base/main.go"

http get $url | save -f main.go

(
    open main.go
    | str replace ":= pocketbase.New()" ":= initApp()"
    | str replace "defaultPublicDir()," "defaultPublicDirFix(),"
    | str replace -r '\s*"github.com/pocketbase/pocketbase"' "\n"
    | save -f main.go
)
