// Include all the necessary libraries.

# include<stdio.h>
# include<stdlib.h>
# include<string.h>



using int main()
{
    printf("def view_selected_events():
    aid=input(\"\n\t\tEnter a Registerd alumini id:-\")
    mycursor.execute(\"select * from selected_events where alu_id=%s\",(aid,))
    res=mycursor.fetchall()
    if len(res)==0:
        print(\"\n\t\tEnter a valid Alumini Id\")
    else:
        for i in res:
            printf(\"\t===================================\")
            printf(\"\t\tYOUR SELECTED EVENTS ARE:\")
            printf(\"\t==================================\")
            printf(\"\t\t ALUMINI ID:-\",i[0])
            printf(\"\t\t ALUMINI NAME:-\",i[1])
            printf(\"\t\tEVENT ID:-\",i[2])
            printf(\"\t\tEVENT NAME:-\",i[3])
            printf(\"\t\tEVENT DATE:-\",i[4])
            printf(\"\t\tEVENT VENUE:-\",i[5])
            printf(\"\t\tWILL ATTEND:-\",i[6])
            printf(\"\t====================================\")
            \n");
      return 0;
}
int main()
{
    printf("def view_personal_details():
           aid=input(\"\t\tEnter a Registered Alumini Id:-\")
           mycursor.execute(\"select * from alureg where alu_id=%s\",(aid,))
           res=mycursor.fetchall()
           if len(res)==0:
           printf(\"\t\tPLEASE ENTER A VALID ALUMINI ID:-\")
           else:
           for i in res:
           printf(\"\t\t================================\")
           printf(\"\t\tYOUR PERSONAL DETAILS ARE\")
           printf(\"\t\t================================\")
           printf(\"\t\tALUMINI ID:-\",i[0])
           printf(\"\t\tALUMINI NAME:-\",i[1]+i[2])
           printf(\"\t\tALUMINI DATE OF BIRTH:-\",i[3])
           printf(\"\t\tALUMINI GENDER:-\",i[4])
           printf(\"\t\tCORRESPONDANCE ADDRESS:-\",i[5])
           printf(\"\t\tOFFICIAL ADDRESS:-\",i[6])
           printf(\"\t\tEMAIL ADDRESS:-\",i[7])
           printf(\"\t\tCONTACT NUMBER:-\",i[8])
           printf(\"\t\tCURRENT CITY:-\",i[9])
           printf(\"\t\tCURRENT COMPANY:-\",i[10])
           printf(\"\t\tDESIGNATION:-\",i[11])
           printf(\"\t\tSESSION:-\",i[12],\"-\",i[13])
           printf(\"\t\tBRANCH NAME:-\",i[14])
           printf(\"\t\t===============================\")
           \n");
    return 0;
}

int main()
{
    printf("def delete_personal_details():
           aid=input(\"\t\tEnter a Registered Alumini Id:-\")
           mycursor.execute(\"select * from alureg where alu_id=%s\",(aid,))
           res=mycursor.fetchall()
           if len(res)==0:
           printf(\"\t\tPLEASE ENTER A VALID ALUMINI ID:-\")
           else:
           mycursor.execute(\"delete from alureg where alu_id=%s\",(aid,))
           constr.commit()
           printf(\"\n\t\tTHE RECORD HAS BEEN DELETED SUCCESSFULLY\")\n");
    return 0;
}

int main()
{
    printf(def upda"te_personal_details():
           aid=input(\"\n\t\tEnter Alumni ID to be edited : \")
           sql=\"select * from alureg where alu_id=%s\"
           ed=(aid,)
           mycursor.execute(sql,ed)
           res=mycursor.fetchall()
           if len(res)==0:
           printf(\"\n\tENTER A VALID ALUMINI ID\")
           else:
           for x in res:
           fld=input(\"Enter the field which you want to edit : \")
           val=input(\"Enter the value you want to set : \")
           sql=\"Update alureg set \" + fld +\"='\" + val + \"' where alu_id='\" + aid + \"'\"
           sq=sql
           mycursor.execute(sql)
           constr.commit()
           printf(\"\n\t\tRECORD HAS BEEN UPDATED SUCCESSFULLY  \")

           sql=\"select * from alureg where alu_id=%s\"
           ed=(aid,)
           mycursor.execute(sql,ed)
           res=mycursor.fetchall()
           for i in res:
           printf(\"\t\t================================\")
           printf(\"\t\tYOUR UPDATED DETAILS ARE\")
           printf(\"\t\t================================\")
           printf(\"\t\tALUMINI ID:-\",i[0])
           printf(\"\t\tALUMINI NAME:-\",i[1]+i[2])
           printf(\"\t\tALUMINI DATE OF BIRTH:-\",i[3])
           printf(\"\t\tALUMINI GENDER:-\",i[4])
           printf(\"\t\tCORRESPONDANCE ADDRESS:-\",i[5])
           printf(\"\t\tOFFICIAL ADDRESS:-\",i[6])
           printf(\"\t\tEMAIL ADDRESS:-\",i[7])
           printf(\"\t\tCONTACT NUMBER:-\",i[8])
           printf(\"\t\tCURRENT CITY:-\",i[9])
           printf(\"\t\tCURRENT COMPANY:-\",i[10])
           print(\"\t\tDESIGNATION:-\",i[11])
           printf(\"\t\tSESSION:-\",i[12],\"-\",i[13])
           printf(\"\t\tBRANCH NAME:-\",i[14])
           printf(\"\t\t===============================\")\n");
    return 0;
}

int main()
{
    printf("while True:
           printf(\"\t====================================================\")
           printf(\"\t\tMAIN MENU\")
           printf(\"\t==================================================\")
           printf(\"\t\t1. ADMIN\")
           printf(\"\t\t2. ALUMINI\")
           print(\"\t\t3. EXIT\")
           ch=int(input(\"\n\t\t Enter Your choice\"))
           if ch==1:
           while True:
           printf(\"\t======================================================\")
           printf(\"\t\tADMIN MENU\")
           printf(\"\t======================================================\")
           printf(\"\t\t1. REGISTER\")
           printf(\"\t\t2. LOGIN\")
           printf(\"\t\t3. EXIT\")
           cho=int(input(\"\n\t\t Enter Your choice\"))
           if cho==1:
           add_admin()
           elif cho==2:
           admin_login()
           elif cho==3:
           break
           if ch==2:
           while True:
           printf(\"\t=====================================================\")
           printf(\"\t\tALUMINI MENU\")
           printf(\"\t====================================================\")
           printf(\"\t\t1. REGISTER\")
           printf(\"\t\t2. LOGIN\")
           printf(\"\t\t3. EXIT\")
           cho=int(input(\"\n\t\t Enter Your choice\"))
           if cho==1:
           register_alumni()
           elif cho==2:
           alu_login()
           elif cho==3:
           break
           if ch==3:
           break\n");
    return 0;
}
