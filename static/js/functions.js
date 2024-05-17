function Browse_Send_Nessus()
{
    var input = document.createElement('input');
    input.type = 'file';

    input.onchange = e => { 

    // getting a hold of the file reference
    var file = e.target.files[0];
    // setting up the reader
    var reader = new FileReader();
    reader.readAsText(file,'UTF-8');

    // here we tell the reader what to do when it's done reading...
    reader.onload = readerEvent => {
        var content = readerEvent.target.result; // this is the content!
        
        data = {'data' : content}
        
        document.getElementById('Browse_Nessus').innerHTML = 'Selected'
        fetch("/Nessus", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
            })
            .then((response) => response.json())
            .then((data) => document.getElementById('Nesout').innerHTML='Successful, please check home folder.')
            .catch((error) => console.error("Error:", error));
    
                }
    }
    
    

    input.click();
    
}

function Browse_Send_Nmap()
{
    var input = document.createElement('input');
    input.type = 'file';

    input.onchange = e => { 

    // getting a hold of the file reference
    var file = e.target.files[0];
    // setting up the reader
    var reader = new FileReader();
    reader.readAsText(file,'UTF-8');

    // here we tell the reader what to do when it's done reading...
    reader.onload = readerEvent => {
        var content = readerEvent.target.result; // this is the content!
        data = {'data' : content}
        document.getElementById('Browse_Nmap').innerHTML = 'Selected'
        fetch("/Nmap", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((data) => document.getElementById('Mapout').innerHTML='Successful, please check home folder.')
        .catch((error) => console.error("Error:", error));

            }
    

    }

    input.click();
    
}