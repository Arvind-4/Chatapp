import { defineConfig } from 'vite';

export default defineConfig({
  root: './src',
  build: {
    target: 'esnext',
    manifest: true,
    polyfillDynamicImport: false,
    minify: true,
    outDir: '../dist', 
  },
});
