/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html","./static/**/*.js", ],
  theme: {
    container: {
      center:true,
      padding: {
        DEFAULT: '2rem',
        sm: '2rem',
        lg : '4rem',
        xl: '5rem',
        '2xl' : '6rem',
      }
    },
  },
  plugins: [],
}

