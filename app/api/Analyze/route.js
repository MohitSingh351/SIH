const { PythonShell } = require('python-shell')

let options = {
    scriptPath: `${__dirname}`,
    args: ["logo.png"],
}

PythonShell.run("main.py", options, (err, res) => {
    if (err) console.log(err)
    if (res) console.log(res)
})