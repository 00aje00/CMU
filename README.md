*Take-home activity for the Containerize task.*

*This README should be completed by the candidate and serves as part of their submission.*

*Feel free to structure this document however you like, so long as it includes the minimum required information: running instructions and sample output.*


**This illustrates the basics on how to dockerize a Flask MySQL application**

# Prerequisites 

- docker
- docker compose
- python3*

## Running Instructions

Clone this repo
- git clone 

Enter the directory
- cd CMU

Run Compose to build the app
- docker compose up -d

Test the output of your api
- curl localhost:8080

## Sample Output
??                                                                 ??
{
  "message": "This is the main endpoint to the cheese rating API."
}
