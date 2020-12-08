create table artigos
(
    id_art         serial not null
        constraint artigos_pkey
            primary key,
    tipo           text,
    titulo         text,
    preco          bigint,
    tempo_para_ver bigint,
    detalhes       text
);

alter table artigos
    owner to lbkoexwzuhsloo;

INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (14, 'Filme', 'Crónicas de Natal', null, 1, 'The story of sister and brother, Kate and Teddy Pierce, whose Christmas Eve plan to catch Santa Claus on camera turns into an unexpected journey that most kids could only dream about.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (16, 'Filme', 'Crónicas de Natal: Parte Dois', null, 1, 'Kate Pierce, now a cynical teen, is unexpectedly reunited with Santa Claus when a mysterious troublemaker threatens to cancel Christmas - forever. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (13, 'Filme', 'Juno', null, 1, 'Faced with an unplanned pregnancy, an offbeat young person makes an unusual decision regarding the unborn child.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (15, 'Filme', 'Life in a Year', null, 1, 'The movie follows 17-year-old Daryn who finds out that his girlfriend is dying. He sets out to give her an entire life in the last year she has left.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (18, 'Filme', 'Happiest Season', null, 1, 'A holiday romantic comedy that captures the range of emotions tied to wanting your family''s acceptance, being true to yourself, and trying not to ruin Christmas.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (11, 'Filme', 'Mulan', null, 1, 'A young Chinese maiden disguises herself as a male warrior in order to save her father.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (19, 'Filme', 'Tenet', null, 1, 'Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (17, 'Filme', 'Hillbilly Elegy', null, 1, 'An urgent phone call pulls a Yale Law student back to his Ohio hometown, where he reflects on three generations of family history and his own future.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (12, 'Filme', 'Sozinho em Casa', null, 1, 'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (20, 'Filme', 'Amor com Data Marcada', null, 1, 'Fed up with being single on holidays, two strangers agree to be each other''s platonic plus-ones all year long, only to catch real feelings along the way.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (2, 'Série', 'The Queen''s Gambit ', null, 2, 'Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (4, 'Série', 'Anatomia de Grey', null, 2, 'A drama centered on the personal and professional lives of five surgical interns and their supervisors.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (10, 'Série', 'Peaky Blinders ', null, 2, 'A gangster family epic set in 1900s England, centering on a gang who sew razor blades in the peaks of their caps, and their fierce boss Tommy Shelby.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (1, 'Série', 'The Mandalorian  ', null, 2, 'The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (9, 'Série', 'Star Wars: The Clone Wars  ', null, 2, 'Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (7, 'Série', 'The Walking Dead', null, 2, 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (6, 'Série', 'The Boys  ', null, 2, 'A group of vigilantes set out to take down corrupt superheroes who abuse their superpowers.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (8, 'Série', 'Star Trek: Discovery', null, 2, 'Ten years before Kirk, Spock, and the Enterprise, the USS Discovery discovers new worlds and lifeforms as one Starfleet officer learns to understand all things alien.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (5, 'Série', 'A Guerra dos Tronos', null, 2, 'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (3, 'Série', 'Vikings ', null, 2, 'Vikings transports us to the brutal and mysterious world of Ragnar Lothbrok, a Viking warrior and farmer who yearns to explore - and raid - the distant shores across the ocean.');