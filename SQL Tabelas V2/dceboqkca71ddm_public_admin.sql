create table admin
(
    codigo_seg       bigint,
    pessoa_id_pessoa serial not null
        constraint admin_pkey
            primary key,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text
);

alter table admin
    owner to lbkoexwzuhsloo;

INSERT INTO public.admin (codigo_seg, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (20, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');