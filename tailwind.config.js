/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html, js}", "./static/styles/**/*.{html, js, css}"],
  theme: {
    screens: {
      'xsm': '324px',
      'xxsm': '478px',
      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
      '3xl': '2000px'
    },
    fontSize: {
      'Tiny': '10px',
      'XSmall': '12px',
      'Small': '14px',
      'Base': '16px',
      'Semi-Medium': '17px',
      'Medium': '18px',
      'Large': '20px',
      'Pre-Xl': '22px',
      'xl': '24px',
      '1xl': '27px',
      '2xl': '30px',
      '3xl': '36px',
      '4xl': '48px',
      '5xl': '60px',
      '6xl': '72px',
      '7xl': '84px',
      '8xl': '96px',
      '9xl': '120px',
      '10xl': '144px',
      '11xl': '168px',
      '12xl': '192px',
      '13xl': '216px',
      '14xl': '240px',
      '15xl': '264px',
      '16xl': '288px',
      '17xl': '312px',
      '18xl': '336px',
      '19xl': '360px',
      '20xl': '384px',
      '21xl': '408px',
      '22xl': '432px',
      '23xl': '456px',
      '24xl': '480px',
      '25xl': '504px',
      '26xl': '528px',
      '27xl': '552px',
      '28xl': '576px',
      '29xl': '600px',
    },
    extend: {
      fontFamily: {
        'Metral-Black': ['Metral-Black', 'sans-serif'],
        'Metral-ExtraBold':['Metral-ExtraBold', 'sans-serif'],
        'Metral-Bold': ['Metral-Bold', 'sans-serif'],
        'Metral-Medium': ['Metral-Medium', 'sans-serif'],
        'Metral-Regular': ['Metral-Regular', 'sans-serif'],
        'Metral-Light': ['Metral-Light', 'sans-serif'],
        'Metral-ExtraLight': ['Metral-ExtraLight', 'sans-serif']
      },
      zIndex: {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '10': '10',
        '1000': '1000',
        '1010' : '1010',
      },
      top: {
        '30': '30%',
      },
      spacing: {
        '30': '30rem',
        '66': '18rem',
      },
      borderRadius: {
        '3.0': '3.0rem',
        '3.8': '3.8rem',
      },
      backgroundColor: ['active'],
      width: ['responsive'],
    },
  },
  plugins: [],
}

