css = '''<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

.styled-span {
  font-family: 'Bebas Neue', cursive;
  font-size: 4em;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background-image: linear-gradient(green, green);
  background-size: 100% 10px;
  background-repeat: no-repeat;
  background-position: 100% 0%;
  transition: background-size .7s, background-position .5s ease-in-out;
}

.styled-span:hover {
  background-size: 100% 100%;
  background-position: 0% 100%;
  transition: background-position .7s, background-size .5s ease-in-out;
}

.text-with-line{
    position: relative;
    padding-left: 20px; /* Adjust as needed */
}

.text-with-line::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%; /* Adjust line height */
    width: 8px; /* Adjust line thickness */
    background-color: green; /* Adjust line color */
}

</style> '''