create table cliente
(
    saldo            bigint default 2000,
    pessoa_id_pessoa serial not null,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text,
    constraint cliente_pkey
        primary key (pessoa_id_pessoa)
);

create unique index cliente_pessoa_email_uindex
    on cliente (pessoa_email);

create table artigos
(
    id_art         serial not null,
    tipo           text,
    titulo         text,
    preco          bigint,
    tempo_para_ver bigint,
    detalhes       text,
    constraint artigos_pkey
        primary key (id_art)
);

create table admin
(
    codigo_seg       bigint,
    pessoa_id_pessoa serial not null,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text,
    constraint admin_pkey
        primary key (pessoa_id_pessoa)
);

create table mensagem
(
    id_msg                 serial not null,
    corpo                  text,
    mensagens_lida         boolean,
    admin_pessoa_id_pessoa bigint,
    assunto                text,
    constraint mensagem_pkey
        primary key (id_msg),
    constraint mensagem_fk1
        foreign key (admin_pessoa_id_pessoa) references admin
);

create table estatistica
(
    id_estatistica        serial not null,
    total_clientes        bigint,
    total_artigos         bigint,
    valor_total_alugados  bigint,
    valor_total_alugueres boolean,
    total_art_por_tipo    bigint,
    tempo_total_alugado   bigint,
    tipo_mais_alugado     text,
    constraint estatistica_pkey
        primary key (id_estatistica)
);

create table historico_artigos
(
    id_art         serial not null,
    preco_anterior bigint,
    data_mudanca   date,
    artigos_id_art bigint,
    constraint historico_artigos_pkey
        primary key (id_art),
    constraint historico_artigos_fk1
        foreign key (artigos_id_art) references artigos
);

create table atores
(
    id_ator       serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint atores_pkey
        primary key (id_ator)
);

create table realizador
(
    id_realizador serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint realizador_pkey
        primary key (id_realizador)
);

create table produtor
(
    id_produtor   serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint produtor_pkey
        primary key (id_produtor)
);

create table aluguer
(
    id_aluguer               serial not null,
    preco                    bigint,
    artigos_id_art           bigint not null,
    cliente_pessoa_id_pessoa bigint not null,
    data                     bigint,
    data_validade            bigint,
    constraint aluguer_pkey
        primary key (id_aluguer),
    constraint aluguer_fk1
        foreign key (artigos_id_art) references artigos,
    constraint aluguer_fk2
        foreign key (cliente_pessoa_id_pessoa) references cliente
);

create table registo_mensagem
(
    id_registo      serial not null,
    mensagens_lidas bigint,
    mensagem_id_msg bigint,
    constraint registo_mensagem_pkey
        primary key (id_registo),
    constraint registo_mensagem_fk1
        foreign key (mensagem_id_msg) references mensagem
);

create table artigos_produtor
(
    artigos_id_art       bigint not null,
    produtor_id_produtor bigint not null,
    constraint artigos_produtor_pkey
        primary key (artigos_id_art, produtor_id_produtor),
    constraint artigos_produtor_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_produtor_fk2
        foreign key (produtor_id_produtor) references produtor
);

create table artigos_realizador
(
    artigos_id_art           bigint not null,
    realizador_id_realizador bigint not null,
    constraint artigos_realizador_pkey
        primary key (artigos_id_art, realizador_id_realizador),
    constraint artigos_realizador_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_realizador_fk2
        foreign key (realizador_id_realizador) references realizador
);

create table artigos_atores
(
    artigos_id_art bigint not null,
    atores_id_ator bigint not null,
    constraint artigos_atores_pkey
        primary key (artigos_id_art, atores_id_ator),
    constraint artigos_atores_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_atores_fk2
        foreign key (atores_id_ator) references atores
);

create table cliente_mensagem
(
    cliente_pessoa_id_pessoa bigint not null,
    mensagem_id_msg          bigint not null,
    constraint cliente_mensagem_pkey
        primary key (cliente_pessoa_id_pessoa, mensagem_id_msg),
    constraint cliente_mensagem_fk1
        foreign key (cliente_pessoa_id_pessoa) references cliente,
    constraint cliente_mensagem_fk2
        foreign key (mensagem_id_msg) references mensagem
);

create table cliente_artigos
(
    cliente_pessoa_id_pessoa bigint not null,
    artigos_id_art           bigint not null,
    constraint cliente_artigos_pkey
        primary key (cliente_pessoa_id_pessoa, artigos_id_art),
    constraint cliente_artigos_fk1
        foreign key (cliente_pessoa_id_pessoa) references cliente,
    constraint cliente_artigos_fk2
        foreign key (artigos_id_art) references artigos
);

create table admin_artigos
(
    admin_pessoa_id_pessoa bigint not null,
    artigos_id_art         bigint not null,
    constraint admin_artigos_pkey
        primary key (admin_pessoa_id_pessoa, artigos_id_art),
    constraint admin_artigos_fk1
        foreign key (admin_pessoa_id_pessoa) references admin,
    constraint admin_artigos_fk2
        foreign key (artigos_id_art) references artigos
);

create procedure aluguer(dataaluguer integer, datafimaluguer integer, precoaluguercents integer, idartigo integer,
                         idpessoa integer)
    language plpgsql
as
$$
declare
    saldoCliente int;

BEGIN
    SELECT saldo
    INTO saldoCliente
    FROM cliente
    WHERE pessoa_id_pessoa = idPessoa;

    IF saldoCliente >= precoAluguerCents THEN
        INSERT INTO aluguer(preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade)
        VALUES (precoAluguerCents, idArtigo, idPessoa, dataAluguer, dataFimAluguer);
        UPDATE cliente SET saldo = saldoCliente - precoaluguercents WHERE pessoa_id_pessoa = idpessoa;
    ELSE
        RAISE EXCEPTION 'Saldo insuficiente';
        RETURN;
    END IF;
END;
$$;

INSERT INTO public.admin (codigo_seg, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (20, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');

INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 3, 'marta@netflox', 'Marta', '$5$rounds=535000$H1/3lCLSvJj1o5OT$w.FoF0VTz3uckKecKyG4tkYpwKaF3cXtJL0978bm7hA');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (200, 5, 'mario@netflox', 'Mário', '$5$rounds=535000$plsbpQOVcHDGpsu1$vCMFUDufGVN0bUFgER277E3ocB3VtJIKIufYss.bSu6');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 7, 'daninandes@', 'DaniMélia', '$5$rounds=535000$ipAqtkpqbIa4Yqdg$J2YtfvNhwslvkjfB/XDoNKnWJZSZv0hmxt3etMh6Gv5');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 8, 'teste@', 'Teste', '$5$rounds=535000$TwuvQojjPNdK1N6i$3MLH4qi3LYa338gdjzdzD7Za3c./BvuXbPu2CLc2WC8');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (34313, 1, '@', 'João', '$5$rounds=535000$d5on8ALzbWCbD1YY$bVPKOcmaixTs6kliordcMMJoKplWHtWDSoTq4k8CZo7');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (12100, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');

INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (2, 'Série', 'The Queen''s Gambit ', 1056, 5, 'Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (17, 'Filme', 'Hillbilly Elegy', 399, 1, 'An urgent phone call pulls a Yale Law student back to his Ohio hometown, where he reflects on three generations of family history and his own future.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (19, 'Filme', 'Tenet', 599, 2, 'Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (13, 'Filme', 'Juno', 399, 3, 'Faced with an unplanned pregnancy, an offbeat young person makes an unusual decision regarding the unborn child.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (15, 'Filme', 'Life in a Year', 599, 1, 'The movie follows 17-year-old Daryn who finds out that his girlfriend is dying. He sets out to give her an entire life in the last year she has left.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (3, 'Série', 'Vikings ', 1199, 6, 'Vikings transports us to the brutal and mysterious world of Ragnar Lothbrok, a Viking warrior and farmer who yearns to explore - and raid - the distant shores across the ocean.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (16, 'Filme', 'Crónicas de Natal: Parte Dois', 399, 2, 'Kate Pierce, now a cynical teen, is unexpectedly reunited with Santa Claus when a mysterious troublemaker threatens to cancel Christmas - forever. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (12, 'Filme', 'Sozinho em Casa', 599, 2, 'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (8, 'Série', 'Star Trek: Discovery', 599, 4, 'Ten years before Kirk, Spock, and the Enterprise, the USS Discovery discovers new worlds and lifeforms as one Starfleet officer learns to understand all things alien.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (1, 'Série', 'The Mandalorian  ', 899, 4, 'The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (20, 'Filme', 'Amor com Data Marcada', 849, 1, 'Fed up with being single on holidays, two strangers agree to be each other''s platonic plus-ones all year long, only to catch real feelings along the way.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (9, 'Série', 'Star Wars: The Clone Wars  ', 899, 8, 'Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (18, 'Filme', 'Happiest Season', 299, 1, 'A holiday romantic comedy that captures the range of emotions tied to wanting your family''s acceptance, being true to yourself, and trying not to ruin Christmas.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (14, 'Filme', 'Crónicas de Natal', 299, 1, 'The story of sister and brother, Kate and Teddy Pierce, whose Christmas Eve plan to catch Santa Claus on camera turns into an unexpected journey that most kids could only dream about.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (7, 'Série', 'The Walking Dead', 1199, 4, 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (10, 'Série', 'Peaky Blinders ', 1200, 6, 'A gangster family epic set in 1900s England, centering on a gang who sew razor blades in the peaks of their caps, and their fierce boss Tommy Shelby.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (4, 'Série', 'Anatomia de Grey', 899, 7, 'A drama centered on the personal and professional lives of five surgical interns and their supervisors.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (5, 'Série', 'A Guerra dos Tronos', 899, 6, 'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (11, 'Filme', 'Mulan', 299, 1, 'A young Chinese maiden disguises herself as a male warrior in order to save her father.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (6, 'Série', 'The Boys  ', 1260, 6, 'A group of vigilantes set out to take down corrupt superheroes who abuse their superpowers.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (21, 'Documentário', 'Alien Worlds', 799, 1, 'Applying the laws of life on Earth to rest of the galaxy, this series blends science facts and fiction to imagine alien life on other planets.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (22, 'Documentário', 'Murder on Middle Beach', 399, 2, 'A young man is determined to solve an unspeakable crime and absolve the people he loves, while looking for answers within his fractured family and community.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (23, 'Documentário', 'Mosul', 1010, 1, 'The gritty, thrilling story of local militias and uneasy allies who banded together to liberate Iraq''s second-largest city of 1.3 million people from ISIS in 2017.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (24, 'Documentário', 'Diego Maradona', 550, 2, 'Constructed from over 500 hours of never-before-seen footage, this documentary centers on the career of celebrated football player Diego Maradona, who played for S.S.C. Napoli in the 1980s.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (25, 'Documentário', 'How to with John Wilson', 199, 1, 'An anxious New Yorker who attempts to give everyday advice while dealing with his own personal issues.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (26, 'Documentário', 'The Social Dilemma ', 1230, 3, 'Explores the dangerous human impact of social networking, with tech experts sounding the alarm on their own creations.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (27, 'Dummy', 'Dummy object', 9999999, 1, 'This is just a dummy to test the feature that prevents rental if no money');

INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (8, 'Dee', 'Baker');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (10, 'Sonequa', 'Martin-Green');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (7, 'Tom', 'Kane');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (1, 'Karl', 'Urban');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (5, 'Norman', 'Reedus');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (9, 'Matt', 'Lanter');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (6, 'Melissa', 'McBride');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (12, 'Anthony', 'Rapp');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (4, 'Andrew', 'Lincoln');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (2, 'Jack', 'Quaid');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (3, 'Antony', 'Starr');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (11, 'Doug', 'Jones');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (13, 'Emilia', 'Clarke');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (18, 'James', 'Pickens');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (21, 'Gustaf', 'Skarsgård');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (16, 'Ellen', 'Pompeo');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (20, 'Alexander', 'Ludwid');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (17, 'Chandra', 'Wilson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (19, 'Katheryn', 'Winnick');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (14, 'Peter', 'Dinklage');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (15, 'Kit', 'Harington');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (29, 'Paul', 'Anderson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (27, 'Carl', 'Weathers');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (30, 'Helen', 'McCrory');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (25, 'Pedro', 'Pascal');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (28, 'Cillian', 'Murphy');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (22, 'Anya', 'Taylor-Joy');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (24, 'Bill', 'Camp');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (26, 'Gina', 'Carano');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (23, 'Chloe', 'Pirrie');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (59, 'Sophie', 'Okonedo');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (60, 'Stuart', 'Armstrong');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (33, 'Li', 'Gong');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (32, 'Donnie', 'Yen');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (34, 'Macaulay', 'Culkin');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (36, 'Daniel', 'Stern');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (31, 'Yifei', 'Liu');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (35, 'Joe', 'Pesci');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (44, 'Jaden', 'Smith');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (46, 'Goldie', 'Hawn');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (39, 'Jennifer', 'Garner');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (49, 'Gabriel', 'Basso');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (47, 'Amy', 'Adams');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (45, 'Nia', 'Long');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (38, 'Michael', 'Cera');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (37, 'Elliot', 'Page');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (48, 'Glenn', 'Close');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (40, 'Kurt', 'Russell');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (43, 'Cara', 'Delevingne');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (42, 'Judah', 'Lewis');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (41, 'Darby', 'Camp');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (55, 'Elizabeth', 'Debicki');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (52, 'Mary', 'Steenburgen');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (57, 'Luke', 'Bracey');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (56, 'Emma', 'Roberts');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (58, 'Kristin', 'Chenoweth');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (51, 'Mackenzie', 'Davis');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (54, 'Robert', 'Pattinson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (50, 'Kristen', 'Stewart');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (61, 'Natalie', 'Batalha');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (62, 'Madison', 'Hamburg');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (66, 'Diego', 'Maradona');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (65, 'Anouar', 'H. Smaine ');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (63, 'Bashar', 'Atiyat');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (64, 'Ali', 'Mula');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (68, 'Claudia', 'Villafañe');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (71, 'Row', 'Low');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (69, 'John', 'Wilson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (70, 'Cynthia', 'Larson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (74, 'Bailey', 'Richardson');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (73, 'Jeff', 'Seibert');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (72, 'Tristan', 'Harris');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (67, 'Pelé', '(Edson Arantes)');
INSERT INTO public.atores (id_ator, primeiro_nome, segundo_nome) VALUES (53, 'John', 'David Washington');

INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (2, 'The quick brown fox jumps over the lazy dog 2 The quick brown fox jumps over the lazy dog 2 The quick brown fox jumps over the lazy dog 2', true, 2, 'NetFLOX 2');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (5, 'The quick brown fox jumps over the lazy dog 5 The quick brown fox jumps over the lazy dog 5 The quick brown fox jumps over the lazy dog 5', true, 2, 'Assunto?');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (4, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu nisl vitae odio commodo viverra porta et ligula. Aliquam pharetra venenatis arcu vitae vestibulum. Proin congue nisl ac nunc consectetur rhoncus. Nulla fermentum vestibulum arcu at cursus. Phasellus feugiat lorem maximus felis tincidunt, in consequat ante varius. Sed nec elit cursus, facilisis sapien at, viverra tortor. Suspendisse felis lacus, pretium ullamcorper ultrices eu, fringilla in mi.', true, 2, 'Lorem ipsum');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (3, 'The quick brown fox jumps over the lazy dog 3 The quick brown fox jumps over the lazy dog 3 The quick brown fox jumps over the lazy dog 3', true, 2, 'Ganhou um vale!');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu nisl vitae odio commodo viverra porta et ligula. Aliquam pharetra venenatis arcu vitae vestibulum. Proin congue nisl ac nunc consectetur rhoncus. Nulla fermentum vestibulum arcu at cursus. Phasellus feugiat lorem maximus felis tincidunt, in consequat ante varius. Sed nec elit cursus, facilisis sapien at, viverra tortor. Suspendisse felis lacus, pretium ullamcorper ultrices eu, fringilla in mi.', true, 2, 'NetFLOX 1');

INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (1, 'Chris', 'Bender');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (2, 'Tarquin', 'Gotch');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (3, 'Joseph', 'Drake');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (4, 'Bill', 'Andrew');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (5, 'Marc', 'Bienstock ');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (6, 'William', 'M. Connor');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (7, 'Marty', 'Bowen');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (9, 'Mary', 'Viola');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (8, 'Emma', 'Thomas');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (11, 'Sara', 'Rodriguez');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (15, 'Larissa', 'Rhodes');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (14, 'Nathan', 'Fielder');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (13, 'Paul', 'Martin');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (12, 'Matt', 'Schrader');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (10, 'Lynn', 'Philpott');

INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (11, 'Niki', 'Caro');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (12, 'Chris', 'Columbus');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (13, 'Jason', 'Reitman');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (15, 'Mitja', 'Okorn');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (14, 'Clay', 'Kaytis');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (19, 'Jonh', 'Whitesell');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (17, 'Clea', 'DuVall');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (18, 'Christopher', 'Nolan');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (16, 'Ron', 'Howard');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (2, 'Scott', 'Frank');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (5, 'David', 'Nutter');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (8, 'Olatunde', 'Osunsanmi');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (9, 'Dave', 'Filoni');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (7, 'Greg', 'Nicotero');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (3, 'Ciaran', 'Donnelly');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (10, 'Colm', 'McCarthy');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (4, 'Rob', 'Corn');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (6, 'Philip', 'Sgriccia');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (1, 'Rick', 'Famuyiwa ');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (20, 'Suzy', 'Boyles');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (21, 'Madison', 'Hamburg');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (22, 'Daniel', 'Grabriel');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (23, 'Asif', 'Kapadia');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (24, 'John', 'Wilson');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (25, 'Jeff', 'Orlowski');

INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 25);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 26);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 27);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 22);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 23);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 24);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 19);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 20);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 21);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 18);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 17);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 16);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 15);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 14);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 13);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 1);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 2);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 29);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 3);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 30);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 4);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 5);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 6);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 10);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 11);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 12);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 7);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 8);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 9);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 28);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 31);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 32);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 33);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 34);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 35);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 36);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 37);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 38);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 39);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 40);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 41);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 42);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 43);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 44);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 45);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 40);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 46);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 41);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 47);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 48);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 49);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 50);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 51);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 52);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 53);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 54);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 55);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 56);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 57);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 58);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (22, 62);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (23, 63);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (23, 64);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (23, 65);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (21, 60);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (21, 59);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (21, 61);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (24, 66);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (24, 67);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (24, 68);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (25, 69);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (25, 70);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (25, 71);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (26, 72);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (26, 73);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (26, 74);

INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (11, 1);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (12, 2);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (13, 3);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (14, 4);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (15, 5);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (16, 4);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (17, 6);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (18, 7);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (19, 8);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (20, 9);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (21, 10);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (22, 11);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (23, 12);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (24, 13);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (25, 14);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (26, 15);

INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (11, 11);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (12, 12);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (13, 13);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (14, 14);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (15, 15);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (16, 12);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (17, 16);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (18, 17);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (19, 18);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (20, 19);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (1, 1);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (2, 2);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (3, 3);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (4, 4);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (5, 5);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (6, 6);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (7, 7);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (8, 8);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (9, 9);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (10, 10);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (21, 20);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (22, 21);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (23, 22);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (24, 23);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (25, 24);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (26, 25);

INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (7, 550, 24, 1, 1607651672, 1608864872);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (8, 899, 4, 1, 1607652655, 1611889855);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (9, 1230, 26, 1, 1607675419, 1609493419);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (10, 1056, 2, 1, 1607677991, 1610705591);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (11, 599, 15, 1, 1607701951, 1608310351);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (12, 899, 9, 1, 1607701973, 1612543973);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (13, 1200, 10, 1, 1607702964, 1611335364);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (5, 899, 3, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (4, 899, 1, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (3, 899, 3, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (2, 899, 12, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (1, 899, 18, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (6, 899, 21, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (14, 1023, 25, 1, 1607722443, 1608935643);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (15, 849, 20, 1, 1607724947, 1608333347);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (16, 799, 21, 1, 1607725270, 1608333670);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (17, 599, 12, 1, 1607786799, 1608999999);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (18, 599, 19, 1, 1607790860, 1609004060);