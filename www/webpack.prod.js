const path = require('path');
const { merge } = require('webpack-merge');
const TerserPlugin = require('terser-webpack-plugin');
const commonConfig = require('./webpack.common.js');

for (const idx in commonConfig.module.rules) {
  if (commonConfig.module.rules[idx].loader === "ts-loader") {
    if (!commonConfig.module.rules[idx].options) {
      commonConfig.module.rules[idx].options = {};
    }
    commonConfig.module.rules[idx].options.configFile = path.resolve(__dirname, 'tsconfig.prod.json');
    break;
  }
}

module.exports = merge(commonConfig, {
  mode: 'production',
  optimization: {
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          format: {
            comments: false,
          },
        },
        extractComments: false,
      }),
    ],
  },
});