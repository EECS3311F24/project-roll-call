/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Nunito', 'sans-serif'],
      },
      colors: {
        custombg: '#D9E5D6', 
        orange: '#FFBE0A',
      },
    },
  },
  plugins: [],
  corePlugins: {
    preflight: true,
  },
}

