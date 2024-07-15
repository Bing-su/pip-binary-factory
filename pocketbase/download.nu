let ver = open pyproject.toml | get project.version
let url = $"https://raw.githubusercontent.com/pocketbase/pocketbase/v($ver)/examples/base/main.go"

(
    http get $url
    | str replace ":= pocketbase.New()" ":= initApp()"
    | str replace "defaultPublicDir()," "defaultPublicDirFix(),"
    | str replace -r '\s*"github.com/pocketbase/pocketbase"' "\n"
    | str replace "ghupdate.MustRegister" "// ghupdate.MustRegister"
    | str replace -r '\s*"github.com/pocketbase/pocketbase/plugins/ghupdate"' ""
    | save -f main.go
)
