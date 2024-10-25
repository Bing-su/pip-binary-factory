let ver = open pyproject.toml | get project.version
let url = $"https://raw.githubusercontent.com/nektos/act/refs/tags/v($ver)/main.go"
http get $url | save -f main.go
