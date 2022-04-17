create or replace package email_pkg is
DECLARE

email_word varchar2(100);

  -- Public function and procedure declarations
  function gen_email(p_first_name VARCHAR2(50),p_last_name VARCHAR2(50), 
    p_email_type VARCHAR2(50))
     return varchar2(100);

end email_pkg;
/
create or replace package body email_pkg is


  -- Function and procedure implementations
  function  gen_email(p_first_name VARCHAR2(50),p_last_name VARCHAR2(50),  p_email_type number) return VARCHAR2(100) is
   
  begin
   IF p_email_type:=1 THEN
     email_word:=lower(substr(p_first_name,1,1))||'.'|| lower(p_last_name) || '@company.lt';
   ELSIF p_email_type:=2 THEN
     email_word:=lower(substr(p_first_name,1,4))|| lower(substr(p_last_name,1,4)) || '@company.lt';
   ELSE 
     email_word:=null
   END IF;
    return  email_word;
  end;




end email_pkg;
/
