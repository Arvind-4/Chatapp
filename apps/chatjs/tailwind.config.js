const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require('cssnano')

const templatePath = '../templates/**/*.html'
const componentPath = './src/**/*.{js,ts,jsx,tsx,html}'

module.exports = {
  mode: 'jit',
  darkMode: 'media',
  content: [templatePath, componentPath],
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
      content: [templatePath, componentPath],
      enabled: true,
    })
  ]
}