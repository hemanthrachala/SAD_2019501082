function formValidation(){

    var username = document.forms["reg"]["name"].value; // get the username from the form to validate
    var password = document.forms["reg"]["password"].value; // get the password from the form to validate
    var email = document.forms["reg"]["email"].value; // get the email from the form to validate
    var number = document.forms["reg"]["number"].value; // get the mobile number from the form to validate

    var f1 = namevalidation(username);
    var f2 = passwordvalidation(password);
    var f3 = emailvalidation(email);
    var f4 = numbervalidation(number);

    if(f1==true && f2==true && f3==true && f4==true) {
        return true;
    }
    else {
        return false;
    }    

    /**
     * this method is for name validation entered by the user 
     * @param  username 
     */
    function namevalidation(username){
        // username should be entered 
        if(username.length < 5) {
            document.querySelector(".namemessage").innerHTML = "Enter the Username";
            return true;
        }else {
            return false;
        }    
    }
    /**This method is to validate password entered by the user
     * @param password
     * @return true if as per specification
     */
    function passwordvalidation(password) {
        var pwd = password;
        var num = 0;
        var capital = 0;
        var small = 0;
        var special = 0;

        if(pwd == "") {
            var msg = "Enter Password";
            document.querySelector(".passmessage").innerHTML = msg;
            return false;
        }
        if(pwd.length < 7 ) {
            msg = "Password should contain atleast 7 characters ";
            document.querySelector(".passmessage").innerHTML = msg;
            return false;
        }

        for(let i=o; i< pwd.length; i++) {

            var c = pwd.charCodeAt(i);

            if(c >= 49 && c <= 57) num++;
            if(c >= 65 && c <= 90) capital++;
            if(c >= 97 && c <= 122) small++;
            if(c == 42 || c == 46|| c == 64|| c == 95) special++
        } 
        if (num >= 1 && capital>=1 && small >= 1 && special >=1) {
            return true;
        }    
        else {
            var msg = "password should contain atleast capital and small alpahbets,number and one special character";
            document.querySelector(".passmessage").innerHTML = msg;
            return false;
        }   

    }  
    /**
     * this method is to validate the email entered by the user.
     * @param email
     */
    function emailvalidation(email) {
        var e_mail = email;
        var part = e_mail.split('@');

        var msg ="Invalid email"
        var atSymbol = e_mail.indexOf('@');
        var dot = atSymbol + part[1].indexOf('.');

        if(atSymbol < 1){
            document.querySelector(".emailmessage").innerHTML = msg;
            return false;
        }

        if( dot <= atSymbol + 2){
            document.querySelector(".passmessage").innerHTML = msg;
            return false;
        }

        if(dot === email.length - 1){
            document.querySelector(".passmessage").innerHTML = msg;
            return false;
        }
        return true;

    } 
    /**
     * this method is to validate the mobile number.
     * @param  number 
     */
    function numbervalidation(number) {

        var len = number.length;

        if ( len < 10 ) {
            msg = "Moblie number should be valid "
            document.querySelector(".numbermessage").innerHTML = msg;
            return false;
        } 
        return true;
    }
}