from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value
    gender = document.querySelector("#gender").value

    document.querySelector("#output").innerText = ""

    message = f"""Profile: 
    Name   : {name}
    Age    : {age}
    Gender : {gender}
    School : {school}

    
    
    Notes:
    {name} is a {age} year old {gender} who studies at {school}.
    """
    display(message, target="output")