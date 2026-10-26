let ver = open pyproject.toml | get project.version
let url = $"https://raw.githubusercontent.com/pocketbase/pocketbase/v($ver)/examples/base/main.go"

(
    http get $url
    | str replace -r '\s*"github.com/pocketbase/pocketbase/plugins/update"' ""
    | str replace -r '\s*"github.com/pocketbase/pocketbase"' "\n"
    | str replace ":= pocketbase.New()" ":= initApp()"
    | str replace "defaultPublicDir()," "defaultPublicDirFix(),"
    | save -f main.go
)
