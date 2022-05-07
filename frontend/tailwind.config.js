const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')

const templatePath = '../web/templates/**/*.html'
const indexpath = './index.html'
// const componentPath = './src/**/*.{js,ts,jsx,tsx}'
const jsPath = './js/**/*.{js,ts}'

module.exports = {
  mode: 'jit',
  darkMode: 'media',
  content: [templatePath, indexpath, jsPath],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    cssnano({
      preset: 'default'
    }),
    purgecss({
      content: [templatePath, indexpath, jsPath],
      enabled: true,
    })
  ]
}