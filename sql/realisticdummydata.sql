--
-- Script was generated by Devart dbForge Data Generator for MySQL, Version 2.4.526.0
-- Product Home Page: http://www.devart.com/dbforge/mysql/data-generator
-- Script date 4/29/2022 7:59:16 PM
-- Target server version: 8.0.19
-- Target connection string: User Id=root;Host=localhost;Database=final;Character Set=utf8
--



SET NAMES 'utf8';
USE final;
--
-- Delete data from the table 'reply'
--
TRUNCATE TABLE reply;
--
-- Delete data from the table 'pet'
--
TRUNCATE TABLE pet;
--
-- Delete data from the table 'post'
--
DELETE FROM post;
--
-- Delete data from the table 'user'
--
DELETE FROM user;

--
-- Inserting data into table user
--
INSERT INTO user(id, username, email, password, fullname, biography) VALUES
(1, 'Trent226', 'Alexia_Dobbins8@example.com', '3', 'Gale949', 'F201D4OFXJ8QSD0EMX466B2WGM7'),
(2, 'Alexandra2015', 'vnlx5987@nowhere.com', '863S3L5G71J8018K47L63LFI110977UF', 'Ohara2004', '7SAZ5477'),
(3, 'Arsenault944', 'Allen@example.com', '85CWN901I03W', 'Alonzo512', '1CIY4Y3ND5PODH9FK5NWYAN8KEAG0K75PX114152KL2M5OFENT7S5MMJ4N4'),
(4, 'Cleary6', 'Bradbury@example.com', 'T705H0T18O9984', 'Ressie658', 'Z5Y79X8MU6QASXWCZ73J5127626014T82'),
(5, 'Adam1966', 'Marci_Peterson485@example.com', '65K8Y93FG6E', 'Alva2028', '0'),
(6, 'Adelina79', 'Tristan.Mcgregor65@example.com', 'G391H6PP5JI', 'Maki144', 'ZK5XVAH08220'),
(7, 'Margorie3', 'fjfn7678@nowhere.com', '8UOX1GP80QK7ICP063HA09', 'Hoyt334', '6E91C2848XZ781454V6A'),
(8, 'Swanson4', 'Abrams@nowhere.com', '9J', 'Desirae866', 'B2'),
(9, 'Lupita4', 'Arndt@example.com', '55105VBNKB9', 'Bachman1', 'S13E19PHY5'),
(10, 'Quintin42', 'Burgess@example.com', '1F8N0V5T2M6V1344PI3', 'Antwan324', '30U4UFL7W83O7R8SN0C6EGCRF63GS65AD5960QCUW4WEQ3SJSD6NV08'),
(11, 'Drummond36', 'StefanieSpring@example.com', 'EX6LAER979', 'Libbie1956', '05F2340JX5ISPFB0UE675N6NU72Q93CSPS54U31'),
(12, 'Milliken2004', 'WendellTalley@example.com', 'Y3E5VTEWLVOR1K', 'Falls2016', '03CI98Z3WSHDR8GN73D3F'),
(13, 'Elliot684', 'Demers@example.com', '6QA9P5GW5217L8EFC9H9K5GD9711H5VL1D57MW22TRK41FH6DZKNSM', 'Abraham137', 'WDBAA4Z351F8801W6AVNZ7G2POT561V38A7210VDWTAWLZUQX8O4D6Y3L4'),
(14, 'Travis2026', 'Marin2@example.com', 'T4MZ4P66', 'Marc37', '6RUIF08TNBG45119'),
(15, 'Emmy64', 'AdelaDoran@example.com', '9ZE1PAH476MIAI273PB8Z9457B9I4', 'Arletha1965', '737I0'),
(16, 'Beau73', 'Cardwell@example.com', 'I12J081TS63CS7467RST3H899O1315VV8W9H8FHAPRRJ683', 'Elizabet2025', '6EQGVYTP787R19E4U685QI2TDJ'),
(17, 'Brunilda8', 'Anaya@example.com', '6ZN1941', 'Woodall819', '5N'),
(18, 'Burgess1955', 'Ferris@nowhere.com', 'L3905EKIK04J1615P5C7IRVCR877', 'Ross2011', 'A5UZTB854JQW2L'),
(19, 'Perkins1963', 'AleciaAlston97@nowhere.com', '02YGQC1B7J5PK5MBW8M79V45F43TLVH324', 'Wingate6', '24X37K31S4LW3TL4K'),
(20, 'Jovan494', 'Alaine.Block7@example.com', 'C97V21702QY1EV56FMS4', 'Dick4', 'D952L9K24PYE34PXLQ9PYMH6'),
(21, 'Jerry175', 'NathanDubose@example.com', '49YZ2SLTCM', 'Fumiko89', 'G081YZ262R1E57HNN58ZFLP61'),
(22, 'Abrams4', 'Brenda_Roderick35@example.com', 'KKZAWYZ5NL8143FZX2C85605US736PSWZ310ZXPW2M869TQ301438RQ83KBG', 'Buckner3', '30K5V8C'),
(23, 'Abe9', 'Gustavo_Monk@example.com', '955312X093931UA588C2R360H44R59491Z', 'Nick485', '5VVTH0FE4PW58'),
(24, 'Scotty85', 'AdelaidaMorrow@nowhere.com', '56DXTLN75BZ927RL8JH28', 'Shaffer2014', '60TCJA5793D24V733M'),
(25, 'Wendi434', 'YungTerrell279@example.com', 'L88L13SR9J9M17', 'Adolfo8', 'LEGS5GW7YXS7C62P23S51SWA7KA3FDGOKIT856VO3Q0TSG4DW85PR8H75X919K4149RN3599B263CEAL85T87S3TABKX83SK3TXZ8JLD53BJ5579LH51C56X31132RRVI0SL6KY0XYN1E'),
(26, 'Branham885', 'Felicita.Amos@example.com', '4L2', 'Kelley1958', '8TA6S1'),
(27, 'Domingo2029', 'Moore2@example.com', '6P6RKX68X3SQ6K09926Q6DJ85E79R524TT686Y5991449ML2L5', 'Alexandria497', 'Y02489S3Y2777UY8X0XTEHQLFRXD09'),
(28, 'Acevedo679', 'Thanh_Bullock522@example.com', 'B8CO622W0T4MLCP02NM45KG21P4M3', 'Jayna2026', '72856037TOGK7A4WK649PYGGBF73M3M4EKT15RT690U'),
(29, 'Malinda2004', 'Hanks@nowhere.com', '3J06P09274MVU82IE94P82D71WKK', 'Charlette17', '5519LRHAR553KIN'),
(30, 'Felix1961', 'uepqajr3283@nowhere.com', 'E9024', 'Ramon2015', '0UW1JGTC078MGLQM7R20QPT'),
(31, 'Aldridge2029', 'Penni_Elrod238@example.com', '25O143MNU5D6A6DA26JEM46F5M6C3F6056NAYRJX', 'Albina1960', 'EJ99'),
(32, 'Hatley1953', 'Abney@nowhere.com', 'DQ', 'Montes36', '2M9Z6T39025UE8848Q30E80JG3JHM5CY0B4E9R5WMY29S'),
(33, 'Arndt91', 'Benson@nowhere.com', '47645SUFMWM', 'Pinckney2010', '3VF5NI86CMT5J75Y0GVES08Z28BMHL5575YWFC5JE17Y0557F3UC2'),
(34, 'Chery1961', 'GeoffreySmalls@nowhere.com', '3N07S5LW12V28N27YDY2', 'Claudio1961', 'TKH1V07BJZ0G21'),
(35, 'Meaghan12', 'amner9923@example.com', '186', 'Cinthia9', '0378'),
(36, 'Bottoms5', 'Ness@example.com', 'TI9Y718MQAKNH881JAYF6Q923EWEF87YYE4', 'Bella766', 'A411NP34PMAZ76FP7876R4YD3TP7UM88I12WD443OIP83T3GG8FREU5L6LLYI2691967Q'),
(37, 'Acevedo1950', 'AdanMount@example.com', '8SK7B5H68H38', 'Pedro874', '2ALDI51F2Q3SU'),
(38, 'Agatha2000', 'Daigle792@example.com', 'P7E611YUVRX40', 'Carvalho1988', 'XL9E2T2LS3O761'),
(39, 'Labbe2006', 'AdamPham@example.com', '12C3', 'Angel91', 'U2A1C11N82PIV78D7ET0Y4N3PV5PV1F1C1MWJ29K76TQUF05'),
(40, 'Alfaro463', 'Blythe.Hahn@example.com', 'E9K92PT47', 'Courtney595', '6DQ08385GWUQXPVI'),
(41, 'Sylvester833', 'Naylor134@example.com', 'F5MBZ2ZJ', 'Correia2001', 'QHW453AE748'),
(42, 'Abernathy2006', 'Errol_Mckeown@example.com', '93KORT46VAA8C', 'Ernestine93', 'HD9AM1'),
(43, 'Angulo2000', 'Liliana.Timm742@example.com', 'A29H9N1M7T57BX92ZD', 'Acker9', '6552W5M24G9DGP0F96K0V787WMDF5JG86NGQ'),
(44, 'Taisha1983', 'DeshawnPMayo61@nowhere.com', '65042383M4Q23Y46Y66B3UB01DM60YVQP7U17G7I96LWWF4X6585NKF10171', 'Reilly187', 'W9665Q92339BJ4L3G40JH2G4Q'),
(45, 'Lemay2002', 'Criswell@example.com', '0X0E92S9I473435537OW', 'Solange2021', '8ST0AQH23PD4ESV'),
(46, 'Minerva855', 'Danuta_Aguirre@example.com', 'LK2', 'Benson995', 'F100W9F6'),
(47, 'Stubblefield4', 'AliceMontanez@example.com', '57PL4AQ2ASJ3H418019QK46M0I', 'Hand4', 'VPON8B208426A10QB35F0188K5EJW'),
(48, 'Jesse1965', 'Acevedo@nowhere.com', 'JT060GDJ3HOG7E92F6', 'Dixie968', '58P8Y19426853'),
(49, 'Mcgrath2019', 'Alethia.S.Murillo@example.com', '8XD3CHQU05YO213I81I980W8ZVUR9OKZ6', 'Austin912', '06575X6M47UU3596051SU4723E471X4637F8JW0MVCNL4F272HU28'),
(50, 'Purdy1990', 'aguh325@nowhere.com', 'QV9D97P1P', 'Ian2027', 'TM868FL3P0XHT617QYT8TSY448I9XD2');

--
-- Inserting data into table post
--
INSERT INTO post(post_id, views, replies, title, content, timestamp, user_id) VALUES
(1, 995276750, 8022, 'Sit beatae doloremque error maxime.', '7782C8I43ZWS95AOEX9BT4SCUB3L183RVH4S728N9C8Q0U4MC7NKW0YQV0U43GV82IUM', '1971-01-22 08:49:34', 7),
(2, 6, 1529629951, 'At molestias obcaecati fugit.', '88XI4E5CAG66579F0DLO082DY04B19TQ096W4A', '1970-01-01 00:00:07', 28),
(3, 8, 1536187488, 'Sed facilis quis omnis ut ab.', 'ZC4918H63E53084IZK5W36SF10M4TKD', '1970-01-01 00:00:09', 27),
(4, 1899, 618424319, 'Nihil odio et earum.', '7KB3MW1', '1970-01-01 00:31:40', 45),
(5, 0, 72516481, 'Itaque voluptatum eligendi et.', 'EF897LN7YI2452P541O3FO4423VHZP9YU39YN', '1970-01-01 00:00:01', 1),
(6, 2103790239, 795971897, 'Sunt assumenda nemo sit.', '393JM7E1D2C', '2013-05-17 15:01:52', 28),
(7, 2103870879, 168803406, 'Fugit recusandae deleniti repellat.', '2X0MP2V9LF89T7J99O5URS798EPL4', '1998-03-11 01:23:20', 21),
(8, 1894427599, 2105340258, 'Officia quod blanditiis modi corrupti.', '363695B1', '2005-04-10 12:25:00', 23),
(9, 960980078, 1137233009, 'Repellat ut temporibus excepturi quas.', 'V7IO5900504WTO14K2BMFA19V23Z8WKM2Y0GRPI32O53IPM4L53F0', '1985-11-19 16:33:06', 42),
(10, 1048455959, 948512833, 'Assumenda quia sed voluptas.', '5ZVNGS01658Y04R068W1A', '1974-10-12 11:51:05', 11),
(11, 2106317778, 1020763037, 'Molestias neque ut suscipit ad magnam.', '5DHY82946YL3C2X5UW6V', '1997-08-03 20:18:51', 4),
(12, 2142449387, 14804451, 'Eaque quasi nesciunt et molestiae.', '72KS4Q0FA2858BDIZ', '1990-01-19 05:53:27', 37),
(13, 251121993, 2146594889, 'Rerum quaerat recusandae voluptates.', 'M06BBVG9531199YU0I076CS3Z1415A7F2701W2RUOW87TJ6HKE032F2GN8Y9F9', '2013-09-15 06:03:09', 8),
(14, 1478612879, 922, 'Rerum magnam soluta autem et atque.', '47BWRVNT', '2019-04-03 19:14:33', 21),
(15, 1620973965, 1367774220, 'A nobis voluptatem at distinctio.', '7PVP3496N3HQZZP462', '2008-07-11 06:15:29', 42),
(16, 762, 1084577221, 'Ut unde provident et.', '3RJJ2S3U5C35S3R33I', '1970-01-01 00:12:43', 3),
(17, 966014338, 1122428558, 'In sed quisquam corrupti ut quis.', '2P756H6QY16A0439Z6ED', '2005-09-14 14:48:05', 5),
(18, 2, 949401591, 'Suscipit magnam qui quia optio modi.', '29H873DP1CYIAF5B7BD0GP07783BK1CE1RBG1V2M90X', '1970-01-01 00:00:03', 24),
(19, 2083476736, 1762481460, 'Voluptate rerum modi et culpa soluta.', '6DFWS33WCJ9V07R5DAD87DDE9NA1732NE0Y88V6FDT8I44N4N71TL647OEYRCB775K170', '1994-08-14 21:25:33', 33),
(20, 1296174267, 530006308, 'Sed sit eveniet sed.', 'K3', '2021-02-22 12:51:17', 33),
(21, 310070596, 1751858783, 'Incidunt quidem voluptatibus fugiat.', 'TR4G21Q24FOANIJM', '2000-12-07 00:43:40', 4),
(22, 4, 1044431970, 'Quaerat deleniti unde tenetur error.', 'WF0BI0326G650D3', '1970-01-01 00:00:05', 32),
(23, 1, 1899167191, 'Nesciunt est corporis ut tenetur.', 'A389B0Q2KN60', '1970-01-01 00:00:02', 22),
(24, 635867792, 1244472781, 'Et dolore vel et error doloremque in.', '25V25I04SEYE29W383V', '2021-07-31 21:05:59', 23),
(25, 1129782944, 697469404, 'Est praesentium dolorem est quos.', '614Q1', '2005-09-25 14:12:42', 47),
(26, 414151155, 640211068, 'Obcaecati placeat voluptate tempora.', '95RFK0U5PU6QN3OC3MN289MU', '2022-03-05 01:39:20', 13),
(27, 887, 427184569, 'Quia omnis sit asperiores eligendi.', '67J163', '1970-01-01 00:14:48', 41),
(28, 1, 1721793939, 'Natus iste nam quo quod perspiciatis.', '83264MQ3', '1970-01-01 00:00:02', 40),
(29, 547, 1093102285, 'Ab saepe et non tempore sapiente.', 'X7D3', '1970-01-01 00:09:08', 37),
(30, 2054615447, 2119250577, 'Commodi totam modi et cupiditate.', 'UC47JJ13R275MQ3719GB', '2022-01-30 04:47:29', 47),
(31, 139930949, 1739526740, 'Et voluptatem eveniet natus molestiae.', 'FVVYD', '1980-08-02 10:34:38', 13),
(32, 1745155803, 103917063, 'Voluptatem iste pariatur asperiores.', '8QW2ZQ', '1979-09-14 03:05:49', 46),
(33, 524, 400167870, 'Natus cumque magni.', '4HC83N05R4W992A5369X2CA36L02M', '1970-01-01 00:08:45', 19),
(34, 1292985865, 175, 'Est consequatur placeat eligendi.', 'RT36HEN808NAN', '2021-06-27 19:14:52', 28),
(35, 53, 455417639, 'Deleniti cupiditate alias sit.', 'S9AYA1WZ3DD2F135A1R431XY', '1970-01-01 00:00:54', 19),
(36, 891, 1413, 'Optio veritatis aspernatur fuga sit.', '1247EC', '1970-01-01 00:14:52', 19),
(37, 1760230758, 1837581437, 'Qui fuga perspiciatis voluptatem.', '0IG1Z', '1998-02-09 22:20:43', 4),
(38, 6, 1371287101, 'Tenetur et tempore ullam voluptatibus.', '41Y15C58P70PH816589', '1970-01-01 00:00:07', 20),
(39, 386517894, 1711847340, 'Quo pariatur qui voluptas qui.', '92G60OMU7955W4K3MS2OVF80H7ZBD300715BD4Y744Z4M36O07TEXD4160', '2021-05-10 18:17:02', 43),
(40, 97, 361870573, 'Sit impedit unde numquam ullam soluta.', 'OPOL39VC4D272J57CF4RN9ND5CGRL218P85XZG7D2X95X4YY0L267H7FTZB68T893828YJSCJ2HA857NE07', '1970-01-01 00:01:38', 1),
(41, 563348624, 1140891913, 'Minus dolorem fuga velit aliquid.', 'VJFF69FK119ZE38H5NWPSQBFF7TF2SHQNX092YA3V', '1992-02-17 18:06:30', 20),
(42, 1393154117, 705407208, 'Iste rerum officia voluptatem.', 'SENY2', '1990-12-27 17:36:05', 17),
(43, 531, 883818579, 'Voluptatem quae qui id culpa odit ad.', '9IB8J711G', '1970-01-01 00:08:52', 12),
(44, 1932267727, 226, 'Hic fugiat corporis voluptates.', '7', '1975-04-26 18:02:58', 15),
(45, 2018990028, 1475710864, 'Dolorem architecto voluptatem error.', '26X1Y1GKG4164A31ASA8CZL7V', '2013-01-29 17:24:55', 4),
(46, 681790041, 7, 'Ut omnis ducimus officia ut vero.', '7L20VIIE', '1976-08-14 13:40:53', 47),
(47, 304, 468, 'Maiores ut quam aliquid.', 'K916J324DRFBU5SM9', '1970-01-01 00:05:05', 8),
(48, 1037879032, 6, 'Sit voluptatem reiciendis assumenda.', '2976P', '2013-12-02 14:06:50', 48),
(49, 1258248603, 95, 'Magni vitae perferendis sed aliquid.', 'YSLUQ7O38FFSDVH2KQBXWPBZ97W6I02', '2015-01-03 07:48:44', 2),
(50, 1034741974, 1863780339, 'Unde voluptatem ratione non cumque.', '6MO5LAV6KA4MLRD2N87U5EJ5G9DT', '2020-09-13 12:21:54', 17);

--
-- Inserting data into table pet
--
INSERT INTO pet(pet_id, species, subspecies, name, color, created_at, tagline, image_file, user_id, biography) VALUES
(1, '00A848', 'WCC9', 'Letha241', 'ZinnwalditeBrown', '1970-01-01 00:07:13', 'JK1E7UKXI020499C3L1XC', 'tedat.png', 29, 'WX2706O1HVS83MC9P3BR3'),
(2, 'KWUQ74', '4WA7S7', 'Mollie1975', 'BabyBlue', '2018-01-20 23:04:30', 'DT0R5U1UZKR', 'entthawitit945.pdf', 24, 'BMO478045Y6JPKAMW7'),
(3, 'T', '0', 'Quintin5', 'TealGreen', '1987-08-13 20:56:22', '5446AFUJ55N0F2', 'oulersent.txt', 26, '4519DA949378HDH6655AUL60Q5I'),
(4, '3NO40J', 'J', 'Kathern49', 'LavenderPink', '1995-11-23 18:45:41', 'L2404P06C8AK68RH6698J642SJG15W8I1800QQVXBB720206WQ19D2VYC568N45PIGRU7XB39F0Q14T4', 'neentou.doc', 2, '26LK2B59274E72YU5163SK83965B3J33QG410H9RW8G59X639ML61NKN5Z8SHSRY937C'),
(5, 'EX', '6O3', 'Felisa221', 'PowderBlue', '2012-06-04 13:50:47', 'W7131B47V3', 'hadverored3.csproj', 13, 'H6U67DJ8ZUW953A0PECZ80L'),
(6, '3LQ8', '9DF', 'Shenita2027', 'RoyalPurple', '1993-10-06 20:36:58', '58826Y6TD7819C70198CDC902', 'enthisesho.pdf', 9, 'J94S69YN96L0461SFG'),
(7, 'SI15', 'L8', 'Arnita2004', 'TerraCotta', '1988-10-22 00:39:53', 'ZOV32C4WY0EJ7G2', 'ouionatst895.doc', 31, '8IOA7E6T104RK1P19955TXF5GH9HAKVOUJH3C1HFRV2FAOF1AU73GM253F59Y4FL7Q'),
(8, 'W4575I527T', '5', 'Woodrow2009', 'CaputMortuum', '2018-10-24 16:41:54', 'D3WPF187092VE56S94S7QQ7S00U2V4I3HJ10Z0PZ43C9MR1R3N379', 'noterentare9.xlsx', 50, '8538XX0'),
(9, 'R7', 'PU7', 'Chantel318', 'Cream', '1970-01-01 00:01:04', 'XS5YG8IO8X3U2', 'asnt.pdf', 6, '9VN059QYV47K7EC4YNY3F1'),
(10, 'D80X', '7823H9ANM99OGB57T081J041U61', 'Aisha2010', 'BabyBlueEyes', '2010-05-13 01:06:32', '2D31VP0JSIS3S81D4JY3Q52M3B3Z9RT3I05V7KE5DS406LPE', 'eaeranot566.txt', 46, 'D5868JJ1763'),
(11, 'E9DL2Q5', '10', 'Christopher1976', 'OutrageousOrange', '2016-03-06 00:19:24', 'E018H365XH11928Q9T19B375C45RWB6SNZ822F65C58CZ1C9MK9185297', 'hatereha.doc', 33, '4PCF2Z25'),
(12, '07C026274Y7E8W7RHCC', '27H', 'Stephan1976', 'Cardinal', '1970-01-01 00:00:05', 'Q54DX2W98IUDDO9GG5EYKFN3LQQCI89T882OW8NO815KE5RCTNGKA610MU517OAPUI9U4988VEP9A2Y464472826Q73B0', 'ithis1.pdf', 40, 'E26Z1L068E21LO4139041I7P55C'),
(13, '5M970G3PJQ', 'EV1F47A9', 'Brinson972', 'Ruby', '1995-07-12 23:47:32', 'XNTN044X1TVQ37N642S9WLC2P304F2TG43086K0AV8NOC9VC8K61', 'reteyoued.txt', 19, '6MG8VP9ZQ7JFHETG71D2C58IE0N115P'),
(14, 'O10XA', '5B5', 'Carpenter1994', 'MediumTaupe', '1970-01-01 00:00:01', 'K91YP07PZ6', 'toithorver.xls', 44, 'C95DK9LVASGV0WR68491PNENJT207D0UZ0'),
(15, '4X306P4', 'BNIL10U9', 'Doyle2', 'DogwoodRose', '2012-11-23 22:01:42', '30U61G6YU7WK963543I657P85958', 'hiitoure.png', 14, 'N2SOMWW7UO76PV40Y8RN453O19B66'),
(16, '4G', 'M5186E4J63SE', 'Johnston1952', 'Crimson', '2017-05-05 07:02:46', '533', 'andinyouand565.png', 25, 'E470'),
(17, 'U1J', 'JZC5016J29XU2', 'Booker6', 'Thistle', '1989-10-12 02:35:23', '7032FFS8787I2MDW7V70LX219P511Y78H43320ZM7048SV5VCTJ9AQ87G8U1Y5903JP7F205YMX096G3H5XP9166A253JLVMIO7858K419I2FQDW4R3324KK0K0ADRP59582S872E15V88IX83E7UK', 'anoulseth.pdf', 20, '6XPL796L8Z14HNAX1300S294C04R3RH'),
(18, '34', '8', 'Carvalho72', 'PrincetonOrange', '1970-01-01 00:15:42', 'L0E43E7V25SK2QAT3917C210OH024', 'hauldall.doc', 36, '7K47BC3EWI3Z856ZCUW1VM2KPCCZ042254166N17TXKH2O8399'),
(19, 'HN4N3', '7N8G8H737987', 'Aguilera1993', 'OxfordBlue', '1992-10-01 19:18:39', '55', 'ereand.xml', 16, '9ECR0Y84XA0RR89GK066377KS730T85B2929V1G5BQM855A5B6RW7UU9'),
(20, 'USVDCUE7', '1K9B7192931C56Z', 'Paris2022', 'DollarBill', '1970-01-01 00:01:23', '50I7A56730B9EH0', 'aronalour.csproj', 16, 'J7813'),
(21, '20Y0', 'ADG8', 'Jerrod1982', 'PrussianBlue', '2010-02-19 18:15:29', 'M567I7M7I2875EW0Z3G4VM3P87LK4OLSW', 'aliontedis.xls', 4, 'B5'),
(22, 'KC', '1848Q', 'Suarez82', 'CrimsonRed', '1973-05-08 03:15:43', 'QHO', 'andnotnt858.png', 29, '9RL4V9ROQ80JMU730S89I97141D92'),
(23, 'ZD65Y4N545K4X', '24', 'Abreu232', 'Ruddy', '1984-11-19 07:40:19', 'TG4628H5SCLD441BPE0537534S71R671IP8M04C06GF3KNFR2OHU0VVO3S4W5N432', 'atthiyoung.doc', 33, 'F0M5G310L86C8GK'),
(24, '0R7Y67CR71T6RNOR', '4M66', 'Shank212', 'LavenderPurple', '2005-01-01 05:56:06', '1QJ385L3Z', 'wated593.xls', 10, '8LWJZUL9569U7MTSACFVY9SNE808659'),
(25, 'E85J6W', 'K86', 'Elise28', 'PacificBlue', '1970-01-01 00:05:13', '828Y44IVBF62UTVS6S88K82C8F6NLK44UKL7RKAZ817F3Q5SMV20VS2D52SV0WE1JKGX381XK22U3M4', 'tedithomehad80.xlsx', 30, 'WM4XEXK0J4N044I4438N5ZY1U4ZGC485'),
(26, '5W4CL4223', '8LQ07I2OL8V', 'Alcala1977', 'PsychedelicPurple', '1990-01-22 15:12:23', '9Y9R05591W29817R1370J137JM2N92SA89475HES3G535AG85Y58K6UVVE587EAWWQ1JT2E9IH4KG856T21Y2D', 'aromehatnt135.xaml', 38, '25AJF24A81J41N37887YAI33SBNY4J4'),
(27, 'I7H', '7KG0Z569M8843208ADSK90R7TA8J', 'Abernathy6', 'Drab', '2007-03-09 01:36:53', '2N86E4UAGYV7RQV52E9UK27MZ7', 'areithonnd53.docx', 34, 'OZ11VTY2MHR'),
(28, 'DXG4M0URM6UI', '7F1B9Z26Z41K16G4H', 'Lindsey295', 'BabyPink', '1970-01-01 00:01:28', 'T1N033RJ6181', 'buthathier119.pdf', 9, 'V1XCURJ6W109KN9I9N3SHC1'),
(29, 'XN059MTLU99367KD9216JD', 'WJQ6', 'Hubert2025', 'CrimsonGlory', '1997-04-06 20:26:47', 'Q7W29GZG0Y38Z88XJW', 'ouromeare936.txt', 13, '0C4F3L8A7LSMXY41ZI093R7K251D83897D2V8VV1D3OO2XJ0PI07LQQ5E35813'),
(30, '8VU80I57Q', 'T', 'Paris24', 'DukeBlue', '1970-01-01 00:01:38', 'PZZ80Z91TLWB965E2I9IK62ZLIDKMH', 'arerehayou.txt', 7, 'R73PL'),
(31, 'U41H49', 'V8QBV8D', 'Muncy1', 'Cyan', '2018-09-26 01:17:33', '6J6DC4CZ2RQBF587CZ683898', 'theareere.txt', 23, '88062ZV9MY763285577J33HFHL58X38IU7V17A'),
(32, '474I0WHI', '5XVJ114IN', 'Jestine2015', 'MediumTealBlue', '2011-11-08 23:16:51', '3PH9X467RCFS01R7T57FHSO2XT2RC1NHIS8X40LKX6K0L4IT2EY0BXI6S', 'atat.png', 30, '1A3C6F27IRECRBN0Y5869FQTI0Y8MSA7TMM6207VC7U8HOTVLAK06844RV1885390B559'),
(33, 'O7SGD3428T', '5N5TX32', 'Alexander3', 'LavenderRose', '1979-11-22 01:46:56', '0478GG2NRX6963I8ZBINU1C64RRD3J49K2DOKXU9CRS2XCK36PK023665K3OH684TUJSY66O81Y3GB0', 'thahaheare999.txt', 25, '68Y92'),
(34, '1A', 'M78', 'Seymour1989', 'CaribbeanGreen', '1970-01-01 01:00:18', 'FH74VW1202ZA14A23P0B2H1O07', 'ashen300.png', 46, '8D51T43K0EV722F'),
(35, 'FZ', 'K11Z5WU56W004GA', 'Lorretta2028', 'MediumTurquoise', '2016-01-03 23:52:19', '694T2UMX699D7D988', 'ngan.xaml', 41, 'V'),
(36, '161', '8YD', 'Andre58', 'PakistanGreen', '2017-06-21 21:08:05', 'H1O5ADD3B', 'andionitwit361.png', 40, '29YKIN5918V0POCP67RKD7BFSE1SJ39404H76VRJ2DUUA3O'),
(37, '240M8', '5', 'Carlson9', 'Puce', '1974-06-02 01:34:28', 'G1ZT497TLJK9FD9EXF6582033VP6UW9JO1WFQUI51C4V66GC7962XK2TL3617P4CDD5654Y2M7R689C6I8F34A4F', 'setearal.csproj', 15, 'RPFN62882NULU0Q9A7K9IE7J24JZ74U1A78FG3928AV14P4Y4DVM92N12IP61WI0VAI'),
(38, 'S34I017R290M4J', 'CJU98056Q810VMJZY88098W937ISU6', 'Jefferies7', 'EarthYellow', '1973-02-24 23:52:54', 'PO5BM91H648YOZ5U9AQKS7RJEFRJ7Y0OQ406JFW8R7700V', 'notforthabut.xlsx', 22, 'U684SB02ML098BW65D6NBCLLTQB075WKXH1P521GW27D218EYVV'),
(39, '504', '48FJ9AGBQ7GY16Y4', 'Verona3', 'BallBlue', '2010-12-04 20:10:05', '2RNE58805BTLT4SAL82D6T9FTK445FH93OJ52U95N3UE008LB814DHREZ6R72I4J4IDL3NK396TO', 'inhis479.txt', 4, '5835T3UPS693Z22N8P38Z598KR5J5'),
(40, 'LMN3ON2', 'NXVP6UL3M29', 'Lanette688', 'ThulianPink', '1999-02-11 17:08:18', '27C7WPQ1Q', 'mestyou.docx', 3, '66NA0K35HG408I18Q39GLS6'),
(41, 'P7TJ382317', 'I6', 'Crystle2000', 'Daffodil', '1981-09-25 10:44:16', 'HI04ZRCBB4Y5396Y83RE69UA475DE47V', 'erallome4.png', 23, 'BSZYZD8KX'),
(42, '2J2Y2', '9UV592K5OF0AD45', 'Weston1954', 'Ecru', '2010-05-15 09:38:32', 'SNIVV7396M453PMOIF860Y12ZW28G6J7KX5A73VZ9KF', 'ithalithin.csproj', 29, 'SCB1H'),
(43, 'LJQ5L613MF3Z', 'J604NYT', 'Abdul134', 'LawnGreen', '2006-06-19 12:23:02', 'D206LFWI14QVPN2P21T7T0ZGJ9I5Q93P3O8S4728K37Y', 'enithmeome665.csproj', 32, 'C94Q58TBF5I9124537G3254I4X228G38394P66Z64ADG82Q1RLS1T47R0082'),
(44, '67O4', '69A60', 'Brigida1989', 'Dandelion', '1977-02-07 04:27:43', '208OP9U3IN525QB57', 'buttedandtio1.txt', 22, '86X15Z6E2BG88D5869B6DHP2K2VAC6A2'),
(45, '3V2009C', '0', 'Christian1985', 'Carmine', '1970-01-01 00:02:22', 'HL6588926086E0', 'eaalereour.xaml', 9, '44469330CDH2B5LA87C8G3D5F9S0J46GCC8VO7584DI4YJ613C'),
(46, '6D1TS5', '8VA8N54', 'Alberto1984', 'MediumVioletRed', '1985-07-25 14:02:56', '36AD6B9NL4ILCN5C49', 'hatonanar.pdf', 34, 'SUB18US9D84T18ZA45N240V'),
(47, '1', 'X', 'Ernesto599', 'RuddyBrown', '2005-04-16 02:24:22', '91MGKMFZDQC7', 'butreterome93.xls', 32, 'B'),
(48, '73UQ6Q', 'T3FQ9H75H', 'Rivka533', 'Lemon', '1986-10-18 05:39:34', 'N35V084E805TR6EK9V6ZTPQ454463P92ZCZGP9IY3J7W7796HRP2V4P9FD4T9R2V585YY4XGYPIV5CBIL200V5', 'waallourera68.txt', 6, '2K3R5BW'),
(49, '56X8', '7E', 'Opal1955', 'PalatinateBlue', '1981-03-07 23:03:40', '5297NWSKJ93093DC3P762425465Q', 'enalenthe.xls', 22, 'B218002377K3VF'),
(50, 'K9', '5IBH6213E3XBTJ164', 'Cornell6', 'Melon', '1970-01-01 02:45:15', 'EVPG6265N7Q5FO0J45407DPM48A8TKJXLEJUS4I', 'eresttiwa917.txt', 29, 'PBDRGQQ8IN6WGV22RD0541GD11D400S7K0C1GVMH3U1MM1FNKN54H5LWS2H16G33');

--
-- Inserting data into table reply
--
INSERT INTO reply(post_id, reply_id, title, content, user_id) VALUES
(50, 13, 'Excepturi perferendis veritatis.', 'K18TQ71R127Y96A0CED6HJAJ5', 1),
(44, 29, 'Corrupti voluptatem explicabo est et.', '3', 2),
(6, 32, 'Dolorum eaque commodi id sed quas et.', 'R4K560IO17I9QA77PD56R3IKV7PC6AW', 3),
(1, 48, 'Perspiciatis ullam quia expedita.', '4J', 4),
(39, 12, 'Aliquid aliquam vero reprehenderit.', 'TZ76061823453S5MU64S1LO2MO7P28012866TRI74EG96772J', 5),
(34, 33, 'Voluptatem pariatur commodi ipsum.', '6087V19', 6),
(32, 4, 'Ipsa et est et qui dolor laborum iste.', '8NVK840093RGXX93QS970Z203H6WTPIE734RZ9E94J4G26SAW', 7),
(47, 4, 'Facilis dolor cum debitis.', '51D256LF2G6', 8),
(7, 19, 'Accusamus sit error ab sapiente.', '75R1S86NKL6I', 9),
(14, 1, 'Labore ratione et.', 'XWA2P', 10),
(45, 48, 'Eum odit omnis porro.', 'L', 11),
(40, 46, 'Harum est quis.', 'F66LLF095HJ739Y7BLOMZ8WBDY5961LASSGZH', 12),
(48, 47, 'Quis odio cumque aperiam omnis culpa.', 'EPR0B02NK5DA43H362T5STBBW3ACS507ZB3UQUXGM80D0SSXMW1HGO', 13),
(27, 26, 'Et debitis et numquam ad ut aperiam.', 'U16057UK8AA25', 14),
(46, 10, 'Accusantium tempore ut voluptatum.', '283BS4OQ6P', 15),
(35, 39, 'Quod perspiciatis omnis laudantium.', 'J', 16),
(2, 19, 'Beatae dolor architecto quam commodi.', 'M8R3UJ3UT', 17),
(41, 24, 'Accusantium nulla aut aliquam culpa.', 'W4', 18),
(20, 11, 'Inventore error voluptate inventore.', 'GC94T8Y6I4O4', 19),
(36, 42, 'Eveniet ea qui est perspiciatis.', 'D4TI5977YA7W32', 20),
(8, 1, 'Veritatis debitis deleniti sunt.', 'W37MSGQD0GAU9968U6E49079IP8CA5YFD22PJ0', 21),
(33, 23, 'Omnis itaque id sed recusandae.', 'S6SG9HB1IAYOY74I8H019H93', 22),
(3, 25, 'Sed labore exercitationem aut et quia.', 'CVUP9XFMJ3OL5KBK4619I1P6ZN4MB6', 23),
(9, 24, 'Eveniet minus quasi sed aut et modi.', 'C7R1O5Z3258T73994W1OW0S6CR7', 24),
(4, 32, 'Sed iste nostrum et doloribus aut.', 'F9K95E51K890H5', 25),
(49, 7, 'Reprehenderit voluptate explicabo.', 'VZYK7HSME8OI7362C02BGXF5W092', 26),
(15, 34, 'Ad in commodi omnis sunt aliquid.', 'N75X2EG4', 27),
(10, 24, 'Illum sunt sit aut asperiores dolor.', 'WB55S357Z3YCD4VB1H65C', 28),
(28, 25, 'Ut voluptatibus corrupti commodi ut.', 'G', 29),
(23, 2, 'Est aperiam ut ullam et sit enim est.', 'ZJF4E8SN', 30),
(42, 16, 'Aliquam ut laudantium molestias.', '669FI8Y4L5J395J1Z922EQ', 31),
(37, 25, 'Est distinctio assumenda ducimus.', '8', 32),
(5, 25, 'Ut laudantium provident consequuntur.', '3WFYMJ885LD40U5WGGATH0E4Q82EA06Q82600546K00J7X', 33),
(11, 24, 'Libero perspiciatis ipsa voluptatem.', '9N043KH6V106U39JL6N0', 34),
(21, 28, 'Nulla omnis molestiae vel.', 'F6K3D68QZETO0E640I5RWK5715MS744EP', 35),
(43, 24, 'Voluptatem molestiae autem.', '7U2S2J6930', 36),
(29, 11, 'Est quo voluptatem.', '82T', 37),
(16, 23, 'Esse itaque suscipit velit error.', '12', 38),
(24, 39, 'Ut aliquam sint.', 'TMTBH9A', 39),
(22, 27, 'Unde eligendi repudiandae vitae ut.', '434I9STO7JX2804', 40),
(30, 43, 'Voluptas aut neque in qui ut.', '2NQ', 41),
(25, 49, 'Aut maxime deleniti.', '0230LN8J1KS200DCG', 42),
(38, 14, 'Vitae sint sit explicabo iste.', '38E8HU394QRXMQRK04Y35U', 43),
(31, 7, 'Sed voluptatum qui aperiam asperiores.', '835', 44),
(17, 10, 'Sunt eaque voluptatibus tempora.', 'W2', 45),
(26, 13, 'Tempora facilis veniam sit error ipsa.', 'Z8F091XS38H2YA29QV7Z6SV89', 46),
(12, 20, 'Sunt possimus enim qui harum enim.', 'YH42822F8W81S320B2GVU94L9G124N4642P0614N6UVN1AO446GC00LX2EMU584OI438KL1F0QDYSP9EC9M5LGUFI4G1P95745', 47),
(18, 26, 'Veniam quia quos libero unde.', 'VR4T1892718T8NB', 48),
(13, 37, 'Accusamus et quia quos.', 'H', 49),
(19, 6, 'Sed error deserunt qui sit voluptatem.', '20ES88L80G16958FT6W5D6YP869EO337332O3LN0JFB0K2CF5CI6M6XQ96JA368516FIIDZ56H6', 50);