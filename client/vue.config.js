module.exports = {
    outputDir: '../server/static',
    devServer: {
        proxy: 'http://localhost:5000'
    }
}