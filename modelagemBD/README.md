#modelagemBD

brM files for ER and logical data model

**->** foi utilizado **varchar(100)** e **varchar(25)** para atributos que possuem texto mas acho que pode ser diminuído

**->** os atributos de porcentagem e  latitude/longitude estão com **float**, os demais estão com **int**.

**->** o atributo ano recebeu o tipo **year**.

**->** quanto às chaves estrangeiras, as opções de **on delete** e **on update** estão com **NO ACTION** ainda, porque teremos que decidir quais serão **cascade**, **restrict** e **set null**.
