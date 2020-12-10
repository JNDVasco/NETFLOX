create table cliente
(
    saldo            bigint default 2000,
    pessoa_id_pessoa serial not null
        constraint cliente_pkey
            primary key,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text
);

alter table cliente
    owner to lbkoexwzuhsloo;

INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 3, 'marta@netflox', 'Marta', '$5$rounds=535000$H1/3lCLSvJj1o5OT$w.FoF0VTz3uckKecKyG4tkYpwKaF3cXtJL0978bm7hA');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 5, 'mario@netflox', 'Mário', '$5$rounds=535000$plsbpQOVcHDGpsu1$vCMFUDufGVN0bUFgER277E3ocB3VtJIKIufYss.bSu6');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 1, '@', 'João', '$5$rounds=535000$d5on8ALzbWCbD1YY$bVPKOcmaixTs6kliordcMMJoKplWHtWDSoTq4k8CZo7');