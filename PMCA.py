#Input: one ICD-10 code
#Output: 0/1,  body system indicator

def flag_icd10(code):
    cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
    mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive = [0]*20
    
    if code.startswith('A15'):  
        pulresp=1 
    if code in ('A171','A1781','A1783'):
        neuro=1
    if code in ('A170','A1782','A1789','A179'):
        neuro=1 
        progressive=1 
    if code.startswith('A180'):
        musculo=1  
    if code.startswith('A181'):
        genito=1 
    if code in('A182','A1885'):
        immuno=1
    if code.startswith('A183'):
        gastro=1       
    if code.startswith('A184'):
        derm=1       
    if code.startswith('A185'):
        opthal=1
    if code.startswith('A186'):
        otol=1
    if code in ('A187','A1881','A1882'):  
        endo=1
    if code in ('A1889','A19'):
        pulresp=1
    if code.startswith('A30'):
        neuro=1
    if code in ('A50','A521','A522','A523','A527','A528',\
                'A529','A53','A81','B100','B900','B91'):
        neuro=1 
        progressive=1 
    if code.startswith('B20'):
        immuno=1 
        progressive=1 
    if code.startswith('B901'):
        genito=1
    if code.startswith('B902'):
        musculo=1
    if code in('B908','B909'):
        pulresp=1
    if code.startswith('B9735'):
        immuno=1 
        progressive=1 
    if code in ('C0','C1','C2','C3','C40','C41',\
                'C43','C4A','C44','C46','C47','C48',\
                'C49','C5','C6','C7','C8','C90',\
                'C910','C911','C913','C914','C916',\
                'C919','C91Z','C92','C93','C940',\
                'C942','C943','C948','C95','C96',\
                'D03','D45','D474','D47Z1'):
        malign=1
    if code in ('D510','D511','D55','D565','D568',\
                'D569','D58','D591','D594','D599','D600',\
                'D608','D609','D63','D640','D641','D642','D643',\
                'D6489','D680','D681','D682','D68312',\
                'D68318','D685','D6861','D6862','D688',\
                'D689','D691','D693','D6941','D6949','D7589'):
        hemato=1 
    if code in ('D560','D561','D570','D571','D572',\
                'D574','D578','D610','D61818','D6182',\
                'D6189','D619','D644','D66','D67',\
                'D68311','D6942','D7581'):
        hemato=1
        progressive=1 
    if code in ('D704','D720','D763','D802','D803',\
            'D804','D805','D808','D838','D839',\
            'D841','D849','D86','D890','D891',\
            'D892','D8989','D899'):
        immuno=1 
    if code in ('D700','D71','D761','D800','D801',\
                'D810','D811','D812','D814','D8189','D819',\
                'D831','D89811','D89813'): 
        immuno=1
        progressive=1 
    if code in ('D820','D8982'):
        genetic=1  
    if code.startswith('D821'):
        genetic=1
        progressive=1 
    if code in ('E018','E030','E031','D032','E034',\
                'E038','E039','E04','E062','E063','E064','E065',\
                'E069','E070','E071','E0789','E079','E08',\
                'E09','E10','E11','E13','E209','E21',\
                'E220','E228','E229','E232','E236','E243',\
                'E248','E249','E25','E260','E261','E2681',\
                'E269','E270','E271','E274','E275','E278',\
                'E279','E28','E29','E310','E318','E319','E45'):
        endo=1  

    if code in ('E00','E230'):
        endo=1
        progressive=1 
    if code.startswith('E312'):
        malign=1       
    if code in ('E40','E43','E440','E50','E52','E53','E54',\
                'E550','E643','E6601','E800','E8020',\
                'E8029','E805','E880','E888'):   
        metab=1  
    if code.startswith('E45'): 
        neuro=1       

    if code in ('E700','E7021','E7029','E7040','E705',\
                'E708','E710','E71120','E7119','E712',\
                'E7131','E7141','E7142','E7144','E7150',\
                'E71510','E71511','E71522','E71529',\
                'E71548','E7200','E7203','E7204','E7209',\
                'E7210','E7211','E7219','E7220','E7222',\
                'E7223','E7229','E723','E728','E729','E7400',\
                'E7401','E7404','E7409','E7421','E7439',\
                'E744','E748','E749','E7502','E7519','E7521',\
                'E7522','E7523','E75249','E7525','E7529',\
                'E754','E7601','E7603','E761','E76219',\
                'E7622','E7629','E763','E770','E771',\
                'E786','E7870','E7871','E7872','E788','E789',\
                'E791','E798','E83','E85','E881','E884'):
        metab=1 
        progressive=1 

    if code in ('E84'): 
        pulresp=1
        progressive=1 
    if code in ('E890','E894','E895'): 
        endo=1  
    if code in ('F04','F070','F1020','F1021','F1096',\
                'F1120','F1121','F1320','F1321','F1420',\
                'F1421','F1520','F1521','F1620','F1621',\
                'F1820','F1821','F1920','F1921','F21',\
                'F22','F24','F31','F32',\
                'F33','F340','F341','F39','F429',\
                'F444','F445','F446','F447','F448',\
                'F449','F450','F4521','F4522','F60',\
                'F63','F6812','F840','F843','F845','F848','F849',\
                'F88','F89','F90','F911','F912',\
                'F913','F918','F919','F951','F952','F981','F984'):
        mh=1  
    if code in ('F200','F201','F202','F203','F205','F208','F25','F50'):
        mh=1
        progressive=1 
    if code in ('F7','F801','F802','F804','F81','F82',\
                'G110','G255','G371','G372','G400',\
                'G401','G402','G403','G404','G405',\
                'G4080','G4082','G409','G40A','G40B',\
                'G474','G50','G510','G511','G512',\
                'G518','G519','G52','G54','G56','G57',\
                'G587','G588','G589','G600','G603',\
                'G608','G609','G6181','G6189','G619',\
                'G620','G621','G622','G63','G7000',\
                'G701','G702','G7080','G7089','G709',\
                'G7114','G7119','G712','G722','G723',\
                'G7289','G729','G733','G737','G801',\
                'G802','G803','G804','G81','G822',\
                'G825','G830','G831','G832','G833',\
                'G834','G835','G8381','G8389','G839',\
                'G900','G904','G905','G908','G909',\
                'G910','G911','G932','G9389','G939',\
                'G969','G990'):
        neuro=1 

    if code in ('F842','G09','G10','G111','G113',\
                'G114','G118','G119','G12',\
                'G14','G23','G241','G253','G2582',\
                'G3181','G3182','G319','G320',\
                'G3281','G35','G360','G370','G375',\
                'G378','G379','G4081','G601','G710',\
                'G7111','G7112','G7113','G800','G808',\
                'G809','G901','G931','G950','G9519',\
                'G9589','G959','G992'):
        neuro=1
        progressive=1 

    if code in ('G4730','G4731','G4733','G4734','G4736','G4737','G4739'):
        pulresp=1 
    if code in ('G4735'):
        pulresp=1 
        progressive=1 
    if code in ('H150','H158','H201','H202', 'H208','H209','H212','H2150','H2151',\
                'H2152','H2154','H2155','H2156',\
                'H218','H270','H2711','H2712','H2713',\
                'H278','H300','H301','H302','H3081',\
                'H309','H310','H3110','H3112','H312',\
                'H313','H314','H318','H319','H330',\
                'H3310','H3319','H332','H333','H334',\
                'H338','H34','H350','H3515','H3516','H3517',\
                'H352','H3530','H3533','H3534','H3535','H3536',\
                'H3537','H3538','H3540','H3541','H3542',\
                'H3543','H3545','H3546','H355','H357',\
                'H3589','H36','H401','H402','H403',\
                'H404','H405','H406','H408','H409','H42',\
                'H430','H432','H433','H4381','H4389',\
                'H4430','H4440','H4450','H46','H4701',\
                'H4703','H4709','H4714','H472','H4731',\
                'H4732','H4739','H474','H475','H476',\
                'H479','H490','H491','H492','H493','H494'):
        opthal=1 

    if code in ('H4891'):
        metab=1
        progressive=1 
    if code in ('H4988','H5000','H5005','H5006',\
                'H5007','H5008','H5010','H5015','H5016',\
                'H5017','H5018','H5030','H5032','H5034',\
                'H5040','H5042','H5043','H505','H5060',\
                'H5069','H5089','H51','H540','H541',\
                'H542','H543','H548','H550','H57'): 
        opthal=1 


    if code in ('H71','H74','H80','H81','H83',\
                'H903','H905','H906','H908',\
                'H913','H918X3','H918X9','H9190',\
                'H9193','H93093','H93099','H9313',\
                'H9319','H9325','H933X3','H933X9'):
        otol=1 
    if code in ('I00','I05','I06','I07',\
                'I080','I088','I089','I09',\
                'I10','I119','I340','I348','I35',\
                'I370','I378','I44','I4510','I4519','I452',\
                'I453','I454','I455','I456','I458',\
                'I459','I471','I472','I48','I4901',\
                'I517','I720','I721','I722','I723',\
                'I724','I728','I729','I7300','I7301',\
                'I7381','I7389','I739','I770','I771',\
                'I773','I774','I775','I776','I778',\
                'I779','I798','I822','I825',\
                'I82709','I82719','I82729','I82891',\
                'I82A29','I82B29','I82C29','I890'):
        cardiac=1 

    if code in ('I110','I200','I21','I24',\
                'I2510','I252','I253','I254','I255',\
                'I258','I259','I127',\
                'I128','I421','I422','I423','I424',\
                'I425','I426','I428','I43','I4902',\
                'I50','I515','I712','I714','I716',\
                'I719','I81','I820'):
        cardiac=1
        progressive=1 


    if code in ('I150','I158'):
        renal=1 
    if code in ('I12','I13'): 
        renal=1
        progressive=1 
    if code in ('I69898','I699'):
        neuro=1 
    if code in ('I630','I631','I632','I65','I671'
                'I674','I675','I676','I677'):
        neuro=1
        progressive=1 
    if code in ('J45','J47','J84842','J950', 'J985','J986'):
        pulresp=1 
    if code in ('J840','J8410','J84111','J84112','J84117','J842','J8483','J84841','J84843','J84848','J8489','J849'):
        pulresp=1
        progressive=1 
    if code in ('K110','K111','K117','K200','K220',\
                'K224','K225','K227','K228','K254',\
                'K255','K256','K257','K264','K265',\
                'K266','K267','K274','K275','K276',\
                'K277','K284','K285','K286','K287',\
                'K3184','K50','K510','K512','K513',\
                'K518','K519','K624','K6282','K632',\
                'K763','K7689','K769','K77',',K811',\
                'K823','K824','K828','K830','K833',\
                'K834','K835','K838','K861','K862',\
                'K863','K868','K900','K901','K902',\
                'K903','K9081','K915'):
        gastro=1 
    if code in ('K73','K74','K754','K761','K766', 'K767'):
        gastro=1
        progressive=1 
    if code in ('L100','L101','L102','L104','L109',\
                'L120','L121','L122','L128','L13',\
                'L574','L744','L89','L904','L940',\
                'L943','L97','L984','L988'):
        derm=1 
    if code in ('M050','M051','M0530','M0560','M060',\
                'M062','M063','M068','M069','M08','M111',\
                'M112','M118','M119','M120',\
                'M303','M311','M313','M314','M316',\
                'M33','M3500','M3501','M353','M45',\
                'M461','M468','M469','M481'):
        immuno=1 
    if code in ('L930','L932','M300','M310','M312',\
                'M321','M340','M341','M349','M355',\
                'M358','M359'):
        immuno=1
        progressive=1 
    if code in ('M100','M103','M104','M109','M1A0','M1A3','M1A4','M1A9'):
        metab=1 
    if code in ('M2105','M2115','M2133','M2137','M215',\
                'M216X','M2175','M2176','M232','M233',\
                'M241','M242','M243','M244','M245',\
                'M246','M247','M248','M278','M400',\
                'M4020','M41','M420','M430','M431',\
                'M438','M460','M471','M4781','M482',\
                'M483','M489','M498','M500','M502',\
                'M503','M5106','M513','M514','M519',\
                'M61','M625','M6289','M720','M722',\
                'M816','M818','M852','M863','M864',\
                'M865','M866','M870','M88',\
                'M890','M894','M897','M908',\
                'M918','M955','M961','M998'):
        musculo=1 
    if code in ('M623','M906','N250'): 
        musculo=1 
        progressive=1 
    if code in ('N02','N04','N05','N08','N13','N1372','N251',\
                'N2889','N312','N318','N319','N320',\
                'N321','N322','N3501','N35028','N351',\
                'N358','N359','N360','N361','N362',\
                'N364','N365','N368','N37','N3942',\
                'N3945','N3946','N39490','N39498'): 
        renal=1 
    if code in ('N03','N18','N19'):
        renal=1
        progressive=1 
    if code in ('N500','N80','N810','N811','N812',\
                'N813','N814','N815','N816','N8181',\
                'N8182','N8183','N8184','N8189','N819',\
                'N820','N821','N824','N825','N828',\
                'N829','N87','N880','N893','N894','N900','N901',\
                'N904','N9081','N99110','N99111',\
                'N99112','N99113','N99114'):   
        genito=1 
    if code in ('P270','P271','P278'):
        pulresp=1
    if code in ('P293'):
        cardiac=1
    if code in ('Q030','Q031','Q038','Q0702'):
        neuro=1 
    if code in ('Q00','Q01','Q02','Q041','Q042',\
                'Q043','Q045','Q048','Q05','Q060',\
                'Q061','Q062','Q063','Q064','Q068',\
                'Q0701','Q0703','Q078','Q079'):
        neuro=1
        progressive=1 
    if code in ('Q100','Q103','Q107','Q110','Q111',\
                'Q112','Q130','Q131','Q132','Q133',\
                'Q134','Q135','Q1381','Q1389','Q140',\
                'Q141','Q142','Q143','Q148','Q150'):
        opthal=1 
    if code in ('Q16','Q171','Q172','Q174','Q178',\
                'Q179','Q180','Q181','Q182','Q189'): 
        otol=1 
    if code in ('Q210','Q211','Q220','Q221','Q222',\
                'Q223','Q229','Q230','Q231','Q232',\
                'Q233','Q238','Q242','Q243','Q244',\
                'Q245','Q246','Q248','Q251','Q252',\
                'Q253','Q254','Q255','Q256','Q257',\
                'Q269','Q282','Q283','Q288'):
        cardiac=1 
    if code in ('Q200','Q201','Q202','Q203','Q204','Q205',\
                'Q208','Q212','Q213','Q218','Q219',\
                'Q225','Q234'):
        cardiac=1
        progressive=1 
    if code in ('Q300','Q301','Q308','Q310','Q311',\
                'Q318','Q321','Q324','Q332','Q338',\
                'Q339','Q34'):  
        pulresp=1 
    if code in ('Q330','Q333','Q334','Q336'):
        pulresp=1 
        progressive=1 
    if code in ('Q351','Q353','Q355','Q359','Q36', 'Q37','Q385'): 
        cranio=1 
    if code in ('Q382','Q383','Q384','Q388','Q390',\
                'Q391','Q392','Q393','Q394','Q395',\
                'Q396','Q398','Q402','Q409','Q41',\
                'Q42','Q431','Q433','Q437','Q438',\
                'Q441','Q458','Q459'):   
        gastro=1 
    if code in ('Q442','Q443','Q445','Q446','Q447', 'Q450'):
        gastro=1 
        progressive=1 
    if code in ('Q540','Q541','Q542','Q543','Q548',\
                'Q549','Q563','Q564','Q6101','Q6210',\
                'Q6211','Q6212','Q6231','Q6239','Q624',\
                'Q625','Q6261','Q6262','Q6263','Q628',\
                'Q640','Q6410','Q6419','Q642','Q644',\
                'Q645','Q646','Q6471','Q6473','Q6474',\
                'Q6475','Q6479','Q649'): 
        genito=1 
    if code in ('Q600','Q601','Q602','Q603','Q604',\
                'Q605','Q6100','Q6102','Q6119',\
                'Q612','Q613','Q614','Q615','Q618',\
                'Q619'):
        genito=1
        progressive=1 
    if code in ('Q650','Q651','Q652','Q653','Q654',\
                'Q655','Q667','Q6689','Q670','Q671',\
                'Q672','Q673','Q674','Q675','Q688',\
                'Q710','Q711','Q712','Q713','Q714',\
                'Q715','Q716','Q7189','Q719','Q720',\
                'Q721','Q722','Q723','Q724','Q725',\
                'Q726','Q727','Q7289','Q73','Q740',\
                'Q760','Q761','Q762','Q763','Q764',\
                'Q774','Q776','Q778','Q780',\
                'Q781','Q782','Q783','Q784','Q788',\
                'Q789','Q796','Q798','Q799'):
        musculo=1 
    if code in ('Q771','Q790','Q791','Q792','Q793''Q794','Q7959'): 
        musculo=1 
        progressive=1 
    if code in ('Q750','Q759'): 
        cranio=1
    if code in ('Q7951'):
        genito=1
    if code in ('Q803','Q804','Q809','Q824'):
        derm=1 
        progressive=1 
    if code in ('Q820'):
        derm=1
    if code in ('Q850'):
        neuro=1
    if code in ('Q851','Q858','Q871','Q872','Q873',\
                'Q8740','Q875','Q8789','Q897','Q898',\
                'Q899','Q90','Q933','Q937','Q9381',\
                'Q9389','Q96','Q970','Q971','Q972','Q978',\
                'Q980','Q981','Q984','Q985','Q987',\
                'Q988','Q992','Q998','Q999'): 
        genetic=1
    if code in ('Q8781','Q8901','Q891','Q892','Q893',\
                'Q894','Q913','Q917','Q928','Q934','Q9388'): 
        genetic=1 
        progressive=1 
    if code in ('R4020','R403','S1410','S1411','S1412',\
                'S1413','S1415','S2410','S2411','S2413',\
                'S2415''S3410','S3411','S3412','S3413','S343'):
        neuro=1 
        progressive=1 

    if code in ('S4801','S4802','S4811','S4812',\
                'S4891','S4892','S5801','S5802',\
                'S5811','S5812','S5891','S5892',\
                'S6841','S6842','S6871','S6872',\
                'S7801','S7802','S7811','S7812',\
                'S7891','S7892','S8801','S8802',\
                'S8811','S8812','S8891','S8892',\
                'S9801','S9802''S9831','S9832', 'S9891','S9892'):
        musculo=1
    if code in ('Z21'): 
        immuno=1
    if code in ('Z430'): 
        pulresp=1
    if code in ('Z431','Z432','Z433','Z434','Z465'):
        gastro=1
    if code in ('Z435','Z436','Z437'):
        genito=1
    if code in ('Z440','Z441'): 
        musculo=1
    if code in ('Z450','Z953'):
        cardiac=1
    if code in ('Z4531'):
        opthal=1
    if code in ('Z45328','Z454','Z461','Z462'):
        neuro=1
    if code in ('Z49','Z940'):
        renal=1
        progressive=1 
    if code in ('Z941','Z95812'):
        cardiac=1 
        progressive=1 
    if code in ('Z942'):
        pulresp=1 
        progressive=1 
    if code in ('Z944','Z9481','Z9482'):
        gastro=1 
        progressive=1 
    if code in ('Z9483'): 
        endo=1 
        progressive=1
        
    condition = cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
                mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive
        
    return condition


#Input: one ICD-9 code
#Output: 0/1,  body system indicator

def flag_icd9(code): 
    cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
    mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive = [0]*20
    
    if code in ['010', '011', '012', '013', '014', '015', '016', '017', '018']:  
        pulresp=1 
    if code.startswith('030'):  
        neuro=1
    if code.startswith('0402'): 
        gastro=1   
    if code in ['042', '043', '044']:   
        immuno=1 
        progressive=1 
    if code in ['046', '0582', '0785']:
        neuro=1
        progressive=1 
    if code.startswith('07953'):
        immuno=1
        progressive=1 
    if code in ['090', '094', '095']:
        neuro=1
        progressive=1 
    if code.startswith('135'):
        immuno=1 
    if code.startswith('1363'):
        pulresp=1   
    if code.startswith('137'):
        pulresp=1
        progressive=1 
    if code in ['138', '139']:
        neuro=1
        progressive=1 
    if code in ['14', '15', '16', '17', '18', '19', '200', '201', '202', '203', '204', '205',\
                '206', '207', '208', '2090', '2091', '2092', '2093', '2097', '23877']:
        malign=1 
    if code.startswith('2377'): 
        neuro=1   
    if code in ['240', '241', '242', '243', '244', '245', '246', '249', '250', '2510', '252',\
                '2530', '2531', '2533', '2534', '2535', '2537', '2538', '254', '255', '256', '257', '258']:
        endo=1
    if code.startswith('2532'):
        endo=1
        progressive=1 
    if code in ['260', '261', '262', '2630', '2632', '264', '265', '266', '267', 
                '2680', '2681', '2682', '273', '274']:
        metab=1  
    if code in ['270', '271', '272', '2750']:
        metab=1
        progressive=1 
    if code.startswith('2770'):
        pulresp=1
        progressive=1 
    if code in ['2771', '2774', '2777']:
        metab=1 
    if code in ['2772', '2773', '2775', '27781', '27782', '27783',\
               '27784', '27785', '27786', '27787', '27788']:           
        metab=1 
        progressive=1 
    if code.startswith('2776'):
        immuno=1 
    if code.startswith('27801'):
        metab=1 
    if code.startswith('279'):
        immuno=1
        progressive=1 
    if code.startswith('2810'):
        hemato=1  
    if code.startswith('282') and code[:4]!='2825':
        hemato=1 
    if code in ['2824', '2826']:
        hemato=1
        progressive=1   
    if code.startswith('283'):
        hemato=1  
    if code.startswith('284'):
        hemato=1 
        if code[:4] !='2841':
            progressive=1 
    if code in ['2850', '28521', '28522', '28529', '2858']:
        hemato=1   
    if code.startswith('286'):           
        hemato=1 
        if code in ['2860', '2861', '2862', '2863']:
            progressive=1   
    if code in ['2871', '2873']:
        hemato=1                        
    if code in ['28802', '2885']:
        immuno=1
    if code in ['28801', '2881', '2882', '2884']:
        immuno=1 
        progressive=1  
    if code in ['28951', '28952', '28953', '28981', '28983', '28989']:
        immuno=1  
    if code in ['2911', '2921', '2940']:
        mh=1 
    if code in ['2950', '2951', '2952', '2953', '2954', '2955', '2956', '2957', '2958']:
        mh=1
        progressive=1 
    if code in ['296', '2971', '2973', '2990', '2991', '2998', '3001', '3003', '3007', '30081'\
                '3010', '3011', '3012', '3013', '3014', '3015', '3016', '3017', '3018', '3039'\
                '3040', '3041', '3042', '3044', '3045', '3046', '3047', '3048', '3049','30722',\
                '30723', '3073', '3077']:  
        mh=1
    if code in ['3071', '30751']:
        mh=1
        progressive=1 
    if code in [ '3100', '3101', '311', '3120', '3121', '3122', '3123', '3124', '3125', \
                '3126', '3127', '31281', '31282', '3129', '31381', '3140', '3141', '3142',\
                '31501', '31502', '3151', '3152', '31531', '31532', '31534', '3154', '3155', \
                '3158', '3159', '317', '3180', '3181', '3182', '319']:
        mh=1 

    if code.startswith('326'):
        neuro=1
        progressive=1 
    if code in ['32720', '32721', '32723', '32724', '32725', '32726', '32727', '32729']:  
        pulresp=1 
    if code.startswith('32725'):
        progressive=1
    if code.startswith('330'):
        neuro=1
        progressive=1 
    if code in ['3313', '3314']:
        neuro=1  
    if code in ['3330', '3332', '3334', '3335', '3336', '33371', '33391']:
        neuro=1
        progressive=1 
    if code.startswith('334'):
        neuro=1
        progressive=1 
    if code in ['335', '336']:
        neuro=1
        progressive=1 
    if code.startswith('337'):
        neuro=1 
    if code in ['340', '341']:
        neuro=1
        progressive=1 
    if code.startswith('342'):
        neuro=1 
    if code.startswith('343'):               
        neuro=1 
        if code in ['3432', '3438', '3439']:
            progressive=1   
    if code.startswith('344'):  
        neuro=1 
        if code.startswith('3440'):
            progressive=1           
    if code in ['345', '347']:    
        neuro=1  
    if code in ['3481', '3482', '3492', '3499']:  
        neuro=1 
        if code.startswith('3481'):
            progressive=1       
    if code in ['350', '351', '352', '353', '354', '355', '356', '357', '358']:
        neuro=1
    if code in ['3590', '3591', '3592']:
        musculo=1
        progressive=1 
    if code in ['3593', '3594', '3595', '3596', '3598', '3599']:
        musculo=1
    if code in ['3602', '3603', '3604', '361', '3620', '3621', '36226', '36227',\
                '36230', '36231', '36232', '36233', '36234', '36235', '36236', '36237',\
                '36240', '36241', '36242', '36243' '36250', '36251', '36252', '36253',\
                '36254', '36255', '36256', '36257', '36260', '36261', '36262', '36263',\
                '36264', '36265', '36266', '36270', '36271', '36272', '36273', '36274',\
                '36275', '36276', '36277', '36285', '363', '3641', '3642', '3645', '3647',\
                '3648', '365', '3690', '3691', '3692', '3693', '3694', '36960', '36961',\
                '36962', '36963', '36964', '36965', '36966', '36967', '36968', '36969',\
                '36970', '36971', '36972', '36973', '36974', '36975', '36976', '377', \
                '3780', '3781', '3782', '3783', '3784', '3785', '3786', '3787', '3788',\
                '3790', '3791', '3792', '3793', '3794', '3795', '3796']:
        opthal=1 
    if code in ['385', '386', '387', '3880', '3881', '3883', '3885']:
        otol=1 
    if code in ['3891', '3892', '3897', '3898', '3899']: 
        neuro=1  
    if code.startswith('390'):
        immuno=1  
    if code in ['393', '394', '395', '396', '397', '398', '401', '402']:  
        cardiac=1 
        if code in ['40201', '40211', '40291']:
            progressive=1
    if code.startswith('403'):  
        renal=1 
        if code in ['40301', '40311', '40391']:
            progressive=1   
    if code.startswith('404'):  
        renal=1 
        if code in ['40401', '40411', '40491', '40402', '40403', '40412', '40413', '40492', '40493']:
            progressive=1   
    if code.startswith('405'): 
        cardiac=1  
    if code in ['410', '411', '412']: 
        cardiac=1
        progressive=1 
    if code.startswith('414') and code[:4]!='4144':
        cardiac=1
        progressive=1 
    if code in ['416', '417']:
        cardiac=1
        progressive=1 
    if code in ['424','426']:
        cardiac=1
    if code.startswith('425') and code[:4]!='4259':
        cardiac=1
        progressive=1 
    if code in ['4270', '4271', '4273', '4274', '42781']:
        cardiac=1 
    if code in ['428', '4291'] and code[:4]!='4289':
        cardiac=1
        progressive=1 
    if code.startswith('4293'): 
        cardiac=1  
    if code in ['433', '4372', '4373', '4374', '4375', '4376', '4377','438']:
        neuro=1
        progressive=1 
    if code in ['441']:
        cardiac=1
        progressive=1 
    if code in ['442', '443']:
        cardiac=1 
    if code.startswith('446'):  
        immuno=1  
        if code in ['4460', '4462', '4463']:                 
            progressive=1 
    if code in ['447']:  
        cardiac=1 
    if code in ['452', '4530']:
        cardiac=1
        progressive=1 
    if code in ['45350', '45351', '45352', '45371', '45372', '45373', '45374', '45375', \
                '45376', '45377', '45379', '4570', '4571', '4572']:
        cardiac=1 
    if code.startswith('493'):
        pulresp=1   
    if code in ['4940', '4941']:
        pulresp=1 
        progressive=1 
    if code.startswith('495'):
        pulresp=1  
    if code.startswith('496'):
        pulresp=1
        progressive=1 
    if code in ['515', '516']:
        pulresp=1 
        progressive=1 
    if code in ['5190', '5193', '5194']: 
        pulresp=1 
    if code.startswith('526'):
        musculo=1  
    if code in ['5270', '5271', '5277']:
        gastro=1 
    if code in ['5300', '53013', '5303', '5305', '5306', '53083', '53084', '53085']:
        gastro=1
    if code in ['531', '532', '533', '534', '5362', '5363']:
        gastro=1 
    if code in ['555', '556', '5651', '5690', '5691', '5692', '56944', '56981']:
        gastro=1  
    if code in ['5714', '5715', '5716', '5718', '5719']:
        gastro=1
        progressive=1 
    if code in ['5723', '5724', '5730']:
        gastro=1 
        progressive=1 
    if code in ['5732', '5734', '5738', '5739', '57511', '5755', '5756', '5758', \
                '5760', '5761', '5764', '5765', '5768', '5771', '5772', '5778',\
                '5790', '5791', '5792', '5794']: 
        gastro=1
    if code.startswith('581'):
        renal=1  
    if code in ['582', '583', '585', '586']:
        renal=1
        progressive=1 
    if code.startswith('5880'):
        musculo=1
        progressive=1 
    if code.startswith('5881'):
        renal=1  
    if code.startswith('591'):
        genito=1  
    if code in ['59371', '59372', '59373', '59382', '5960', '5961','5962','5964',\
                '59652', '59653', '59654', '59655', '598', '5991', '5992', '5993',\
                '5994', '5995', '59981', '59982', '59983']:  
        renal=1
    if code in ['60785', '6083', '617', '618', '619','6221', '6230', '6240', \
                '62920', '62921', '62922', '62923', '62929']:  
        genito=1 
    if code.startswith('694'):
        derm=1 
    if code.startswith('6954'):
        immuno=1
        progressive=1 
    if code in ['7010', '7018', '7050', '707']:
        derm=1 
    if code.startswith('710'):  
        immuno=1
        if code in ['7100', '7108', '7109']:  
            progressive=1 
    if code in ['712', '714']:
        immuno=1   
    if code in ['717', '7180', '7182', '7183', '7184', '7185', '7186', '7187', \
                '7220', '7221', '7222', '7223', '7224', '7225', '7226', '7227', '7228']:
        musculo=1 
    if code in ['720', '721', '725']:
        immuno=1   
    if code in ['7281', '7282', '7286', '7287']:
        musculo=1
    if code.startswith('7283'):
        musculo=1
        progressive=1 
    if code in ['7301', '7310', '7311', '7312', '7313', '7318','7320', '7321', \
                '7330', '7333', '7334', '7337', ]:   
        musculo=1
    if code in ['73605', '73606', '73607', '73631', '73632', '73671', '73672', \
                '73673', '73674', '73675', '73681']:
        musculo=1  
    if code in ['7370', '7371', '7373', '7378', '7379', '7384', '7385', '7386', ]:
        musculo=1  
    if code in ['7400', '7401', '7402', '741']:   
        neuro=1 
        progressive=1 
    if code.startswith('742'):  
        neuro=1 
        if code[:4]!='7423':
            progressive=1     
    if code in ['7430', '7431', '7432', '7434', '7435', '74361', '74362', '74363', '74366', '74369']: 
        opthal=1 
    if code in ['7440', '7442', '7443', '7444', '7449']:
        otolar=1  
    if code in ['7450', '7451', '7452', '7453', '7456', '7457', '7458', '7459']:             
        cardiac=1 
        progressive=1         
    if code in ['7454', '7455']:
        cardiac=1  
    if code.startswith('746') and code[:4]!='7469':     
        cardiac=1 
        if code in ['7462', '7467']:
            progressive=1   
    if code.startswith('7474'):
        cardiac=1
        progressive=1 
    if code in ['7471', '74721', '74722', '74729', '7473', '74781', '74783', '74789']:
        cardiac=1 
    if code.startswith('748'):            
        pulresp=1 
        if code in ['7484', '7485', '7486']:
            progressive=1   
    if code.startswith('749'):
        cranio=1  
    if code in ['7501', '7502', '7503', '7504', '7507', '7509']:
        gastro=1 
    if code in ['7511', '7512', '7513', '7514', '7515', '75160', '7518', '7519']:
        gastro=1 
    if code in ['75161', '75162', '75169', '7517', ]:
        gastro=1
        progressive=1 
    if code in ['75261', '75262', '7527']: 
        genito=1 
    if code in ['7530', '7531']:
        genito=1
        progressive=1  
    if code in ['7532', '7534', '7535', '7536', '7537', '7538', '7539']:
        genito=1 

    if code in ['7540', '7542', '75430', '75431', '75432', '75433', '75434', '75435',\
                '7547', '7552', '7553', '7554', '75553', '75554', '75558']:  
        musculo=1 
    if code in ['7560', '7561', '7563', '7564', '7565', '75683', '75689', '7569']:
        musculo=1
    if code in ['7566', '7567']:
        musculo=1 
        progressive=1 
    if code.startswith('7570'):
        derm=1 
    if  code in ['7571', '75731']:
        derm=1
        progressive=1  
    if code in ['7580', '7581', '7582', '7583', '7585', '7586', '7587', '7588', '7589']:  
        genetic=1
    if code in ['7581', '7582', '75831', '75833']:
        progressive=1 
    if code.startswith('759'):  
        genetic=1 
        if code in ['7590', '7591', '7592', '7593', '7594', '7596']:
            progressive=1 
    if code.startswith('7707'):
        pulresp=1 
    if code in ['78001', '78003']:
        neuro=1
        progressive=1 
    if code in ['78051', '78053', '78057']:    
        neuro=1
    if code in ['78833', '78834', '78837', '78838', '78839']:
        genito=1
    if code in ['887', '896', '897']:
        musculo=1 
    if code in ['9066', '9067', '9068']: 
        musculo=1 
    if code.startswith('952'):
        neuro=1
        progressive=1 
    if code.startswith('V08'):
        immuno=1
    if code.startswith('V151'):
        cardiac=1  
    if code.startswith('V420'):
        renal=1
        progressive=1 
    if code.startswith('V421'):   
        cardiac=1 
        progressive=1 
    if code.startswith('V422'):
        cardiac =1           
    if code.startswith('V426'): 
        pulresp =1
        progressive=1 
    if code in ['V427', 'V4284']:
        gastro=1 
        progressive=1 
    if code.startswith('V4281'):
        hemato=1
        progressive=1 
    if code.startswith('V4283'):
        endo=1
        progressive=1 
    if code.startswith('V4322'):
        cardiac =1
        progressive=1 
    if code in ['V520', 'V521']:
        musculo=1   
    if code in ['V530', 'V532']:
        neuro=1 
    if code.startswith('V533'):
        cardiac=1
    if code.startswith('V535'):
        gastro=1
    if code.startswith('V550'):
        pulresp=1
    if code in ['V551', 'V552', 'V553', 'V554']: 
        gastro=1
    if code in ['V555', 'V556', 'V557']:
        genito =1
    if code in ['V560', 'V561', 'V562', 'V568']:
        renal=1 
        progressive=1 
    if code in ['V5781', 'V5789']:
        musculo=1
        
    condition = cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
                mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive
        
    return condition


#Input: 1) patient_claims: a list of claims for a given patient. 2) a list of ICD-9/10 indicator flags (one flag for each claim)
#Output: 1,2,3,  patient condition

def PMCA_less(patient_claims, patient_claims_flags):
    anycardiac, anycranio, anyderm, anyendo, anygastro, anygenetic, anygenito,\
    anyhemato, anyimmuno, anymalign, anymetab, anymusculo, anyneuro, anyopthal,\
    anyotol, anyotolar, anypulresp, anyrenal,anymh, anyprogressive = [0]*20

    anycardiac2, anycranio2, anyderm2, anyendo2, anygastro2, anygenetic2,\
    anygenito2, anyhemato2, anyimmuno2, anymalign2, anymetab2, anymusculo2,\
    anyneuro2, anyopthal2, anyotol2, anyotolar2, anypulresp2, anyrenal2, anymh2 = [0]*19

    cardiac2h, cranio2h, derm2h, endo2h, gastro2h, genetic2h, genito2h, \
    hemato2h, immuno2h, malign2h, metab2h, musculo2h, neuro2h, opthal2h,\
    otol2h, otolar2h, pulresp2h, renal2h, mh2h = [0]*19
    
    condition = [0]*20
    for diag_codes, icd10_flag in zip(patient_claims, patient_claims_flags):
        if icd10_flag==0:
            for code in diag_codes:
                tmp = flag_icd9(code)
                condition = [x + y for x, y in zip(condition, tmp)]
        if icd10_flag ==1:
            for code in diag_codes:
                tmp = flag_icd10(code)
                condition = [x + y for x, y in zip(condition, tmp)]
        condition = [1 if x else 0 for x in condition]
        
        cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
        mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive = condition
        
        if cardiac==1:
            anycardiac=1
            anycardiac2+1
        if cranio==1:
            anycranio=1
            anycranio2+1
        if derm==1:
            anyderm=1
            anyderm2+1
        if endo==1:
            anyendo=1
            anyendo2+1
        if gastro==1:
            anygastro=1
            anygastro2+1
        if genetic==1:
            anygenetic=1
            anygenetic2+1
        if genito==1:
            anygenito=1
            anygenito2+1
        if hemato==1:
            anyhemato=1
            anyhemato2+1
        if immuno==1:
            anyimmuno=1
            anyimmuno2+1
        if metab==1:
            anymetab=1
            anymetab2+1
        if musculo==1:
            anymusculo=1
            anymusculo2+1
        if neuro==1:
            anyneuro=1
            anyneuro2+1
        if pulresp==1:
            anypulresp=1
            anypulresp2+1
        if renal==1:
            anyrenal=1
            anyrenal2+1
        if opthal==1:
            anyopthal=1
            anyopthal2+1
        if otol==1:
            anyotol=1
            anyotol2+1
        if otolar==1:
            anyotolar=1
            anyotolar2+1
        if mh==1:
            anymh=1
            anymh2+1
        if progressive==1:
            anyprogressive=1
        if malign==1:
            anymalign=1 
            
    scount_less = anycardiac + anycranio + anyderm   + anyendo  + anygastro  + anygenetic + \
                  anygenito  + anyhemato + anyimmuno + anymetab + anymusculo + anyneuro   + \
                  anypulresp + anyrenal  + anyopthal + anyotol  + anyotolar  + anymh
    
    if scount_less >= 2 or anyprogressive == 1 or anymalign == 1:
        cond_less = '3 Complex Chronic'
    elif scount_less == 1:
        cond_less = '2 Non-complex Chronic'
    else:
        cond_less = '1 Non-Chronic'
        
    return cond_less

#Input: 1) patient_claims: a list of claims for a given patient. 2) a list of ICD-9/10 indicator flags (one flag for each claim)
#Output: 1,2,3,  patient condition
#The model is different from the previous one as the input data source might be different

def PMCA_more(patient_claims, patient_claims_flags):
    anycardiac, anycranio, anyderm, anyendo, anygastro, anygenetic, anygenito,\
    anyhemato, anyimmuno, anymalign, anymetab, anymusculo, anyneuro, anyopthal,\
    anyotol, anyotolar, anypulresp, anyrenal,anymh, anyprogressive = [0]*20

    anycardiac2, anycranio2, anyderm2, anyendo2, anygastro2, anygenetic2,\
    anygenito2, anyhemato2, anyimmuno2, anymalign2, anymetab2, anymusculo2,\
    anyneuro2, anyopthal2, anyotol2, anyotolar2, anypulresp2, anyrenal2, anymh2 = [0]*19

    cardiac2h, cranio2h, derm2h, endo2h, gastro2h, genetic2h, genito2h, \
    hemato2h, immuno2h, malign2h, metab2h, musculo2h, neuro2h, opthal2h,\
    otol2h, otolar2h, pulresp2h, renal2h, mh2h = [0]*19
    
    condition = [0]*20
    for diag_codes, icd10_flag in zip(patient_claims, patient_claims_flags):
        if icd10_flag==0:
            for code in diag_codes:
                tmp = flag_icd9(code)
                condition = [x + y for x, y in zip(condition, tmp)]
        if icd10_flag ==1:
            for code in diag_codes:
                tmp = flag_icd10(code)
                condition = [x + y for x, y in zip(condition, tmp)]
        condition = [1 if x else 0 for x in condition]
        
        cardiac, cranio, derm, endo, gastro, genetic, genito, hemato, immuno, malign,\
        mh, metab, musculo, neuro, opthal, otol, otolar, pulresp, renal, progressive = condition
        
        if cardiac==1:
            anycardiac=1
            anycardiac2+1
        if cranio==1:
            anycranio=1
            anycranio2+1
        if derm==1:
            anyderm=1
            anyderm2+1
        if endo==1:
            anyendo=1
            anyendo2+1
        if gastro==1:
            anygastro=1
            anygastro2+1
        if genetic==1:
            anygenetic=1
            anygenetic2+1
        if genito==1:
            anygenito=1
            anygenito2+1
        if hemato==1:
            anyhemato=1
            anyhemato2+1
        if immuno==1:
            anyimmuno=1
            anyimmuno2+1
        if metab==1:
            anymetab=1
            anymetab2+1
        if musculo==1:
            anymusculo=1
            anymusculo2+1
        if neuro==1:
            anyneuro=1
            anyneuro2+1
        if pulresp==1:
            anypulresp=1
            anypulresp2+1
        if renal==1:
            anyrenal=1
            anyrenal2+1
        if opthal==1:
            anyopthal=1
            anyopthal2+1
        if otol==1:
            anyotol=1
            anyotol2+1
        if otolar==1:
            anyotolar=1
            anyotolar2+1
        if mh==1:
            anymh=1
            anymh2+1
        if progressive==1:
            anyprogressive=1
        if malign==1:
            anymalign=1 
            
    if anycardiac2 >=2: 
        cardiac2h=1 
    if anycranio2>=2: 
        cranio2h =1 
    if anyderm2 >=2: 
        derm2h=1 
    if anyendo2 >=2:
        endo2h=1 
    if anygastro2>=2:
        gastro2h =1 
    if anygenetic2 >=2:
        genetic2h=1 
    if anygenito2>=2:
        genito2h =1 
    if anyhemato2>=2: 
        hemato2h =1 
    if anyimmuno2>=2:
        immuno2h =1 
    if anymetab2>=2:
        metab2h= 1 
    if anymusculo2 >=2: 
        musculo2h=1 
    if anyneuro2>=2: 
        neuro2h= 1 
    if anyopthal2>=2: 
        opthal2h =1 
    if anyotol2 >=2: 
        otol2h=1 
    if anyotolar2>=2: 
        otolar2h =1 
    if anypulresp2 >=2:
        pulresp2h=1 
    if anyrenal2>=2:
        renal2h=1 
    if anymh2 >=2:
        mh2h=1 
    
    scount_more= cardiac2h + cranio2h + derm2h   + endo2h   + gastro2h  + genetic2h + genito2h + \
                  hemato2h  + immuno2h + metab2h  + musculo2h + neuro2h  + pulresp2h + renal2h  + \
                  otol2h    + otolar2h + opthal2h + mh2h

    if scount_more >= 2 or anyprogressive ==1 or anymalign ==1:
        cond_more='3 Complex Chronic'
    elif scount_more== 1:
        cond_more='2 Non-complex Chronic'
    else:
        cond_more='1 Non-Chronic'

    return cond_more