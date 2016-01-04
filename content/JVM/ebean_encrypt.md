Title: Ebean encryption
Tags: play,ebean,java 
Author: Charles
Summary: enabling encrytion/decryption in Ebean.
Date: 2015-05-26

If you want to encrypt a database field and you happen to use Play-Framework 2.x, Mysql and Ebean for ORM, this blog post will help you achieve just that.

Now the best way to achieve this is to use `@encrypt` JPA annotation on the model field. Using this annotation would be make the process of encryption/decryption completely transparent to the rest of your codebase. Apart from the model class no other part of your code has to be aware of this process. So for example if you are encrypting a field called password in your model this is how it would look like.

```
    @Encrypted
    public String password;
```

Though the field's type is String, the corresponding database field type won't be `CHAR` or `VARCHAR` as you would expect. Since we are encrypting the field, database type will be binary or byte or another equivalent type supported by the database. For My-SQL it was `VARBINARY`. If you want to override the type to say `VARCHAR` you can use the JPA annotion property like this `@Column(columnDefinition="varchar(50)")`.

Now any reversible encryption/decryption algorithm requires a key this key was supposed to be set by defining the key in applications.conf file or ebean.properties file in your Play application. But due to a yet to be resolved bug in the framework we will have to take a work around as posted in this [SO Post](http://stackoverflow.com/questions/15800453/play-framework-2-1-java-ebean-encrypted-annotation-errors)


```
package models;
import com.avaje.ebean.config.ServerConfig;     
import com.avaje.ebean.event.ServerConfigStartup;     
import com.avaje.ebean.config.EncryptKey;       
import com.avaje.ebean.config.EncryptKeyManager; 

public class CustomServerConfigStartup implements ServerConfigStartup { 

    @Override 
    public void onStart(ServerConfig serverConfig) {     
          serverConfig.setEncryptKeyManager(new BasicEncryptKeyManager());     
    }     
} 

class BasicEncryptKeyManager implements EncryptKeyManager{ 

 @Override 
 public EncryptKey getEncryptKey(String tableName, String columnName) {     
       return new CustomEncryptKey(tableName, columnName);     
 } 

 @Override 
 public void initialise() { 
     //Do nothing (yet)
 } 

} 

class CustomEncryptKey implements EncryptKey{ 

   private String tableName;

   private String columnName;

   public CustomEncryptKey(String tableName, String columnName){
      this.tableName = tableName;
      this.columnName = columnName;
   }

 @Override 
 public String getStringValue() {     
        return play.Configuration.root().getString("application.secret") + "::" + this.tableName + "::" + this.columnName;      
 }     
}
```


Make sure this new class is defined in the same package where your target model (the one where compression is applied) is located. Make note that this encryption is supported by Ebean only for String and Date fields of your model. Now if you had to say manually decrypt and encrypted field from your SQL client or vice versa you can use the following SQL queries.

#####decrypt:

`SELECT CAST(AES_DECRYPT(encrypted-field,'my-encryption-key') as CHAR(50)) from table;`

#####encrypt:

`SELECT AES_ENCRYPT(encrypted-field,'my-encryption-key') from table;`

In case you are using H2-database for development, use the below queries.

#####decrypt:
`SELECT TRIM(CHAR(0) FROM UTF8TOSTRING(DECRYPT('AES', STRINGTOUTF8('<encryption-key>'), '<text to be encrypted>'))) from table`

#####encrypt:
`SELECT ENCRYPT('AES', STRINGTOUTF8('<encryption-key>'), STRINGTOUTF8('<text to be encrypted>')) from table;`


