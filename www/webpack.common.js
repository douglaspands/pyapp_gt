const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const glob = require('glob');

const FOLDER_JS = "src/js";
const FOLDER_SASS = "src/scss";
const FOLDER_DIST = "static";

module.exports = {
  entry: (() => {
    const entries = Object.assign({},
      getDynamicEntries(`./${FOLDER_JS}/**/*.js`),
      getDynamicEntries(`./${FOLDER_SASS}/**/*.scss`)
    )
    return entries;
  })(),
  output: {
    path: path.resolve(__dirname, FOLDER_DIST),
    filename: '[name].bundle.js',
  },
  resolve: {
    extensions: ['.js', '.json'],
  },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
  ],
};


function getDynamicEntries(pattern) {
  const files = glob.sync(pattern);
  const entries = {};
  files.forEach(file => {
    const entryKey = (file
      .replace(/^.*src[\/\\]/, '')
      .replace(/\.[a-zA-Z0-9]+$/, '')
      .replace(/^scss/, 'css'));
    entries[entryKey] = `./${file}`;
  });
  return entries;
}
