const path = require('path');
const { merge } = require('webpack-merge');
const commonConfig = require('./webpack.common.js');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin')

commonConfig.plugins.push(
  new BrowserSyncPlugin({
    open: false,
    host: 'localhost',
    port: 3000,
    proxy: "http://127.0.0.1:8000"
  })
);

module.exports = merge(commonConfig, {
  mode: 'development',
  watch: true,
  devtool: 'inline-source-map',
  watchOptions: {
    poll: true,
  },
});
