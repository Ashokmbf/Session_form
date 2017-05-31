Session_form Documentation
===============================================================================================================================
MySQL

	Staging
		
		mysql --host=173.194.248.243 --user=root --password 
	
	Live
		
		mysql --host=173.194.248.243 --user=root --password

	Privileges

		grant all privileges on test.* to 'root'@'localhost' identified by 'password';
		grant all privileges on audiodb.* to 'audiotube'@'%' with grant option;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Design

      1)Userdetails(1st page)
      2)Qualification(2nd page)
      3)Preview= 1+2  (3rd page)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
30/5/2017

    modified:   app1/views.py
	modified:   app1/views.pyc
	modified:   static/Css/qualification.css
	modified:   static/Css/user.css
	modified:   templates/qualification.html
	modified:   templates/user_details.html

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Git Store Credentials


	$ git config credential.helper store
	$ git push http://example.com/repo.git
	Username: <type your username>
	Password: <type your password>

	[several days later]
	$ git push http://example.com/repo.git
	[your credentials are used automatically]
