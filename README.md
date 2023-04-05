# ITEC CTF 2023

# Crypto

### O scrisoare pierdută - FeDEX - done
- descriere: **Cetățeanul turmentat iți inmana o scrisoare de amor. Insă in forma ei actuala, nu poate fi folosită drept șantaj. O poti tu oare desluși?**
- flag: **ITEC{https://youtu.be/niiYWyglQMM}**
- deploy: `cd ~/path ; docker-compose up`

### Bișnițar - FeDEX - done
- descriere: **Un negustor isi intinde masa, in fiecare dimineată, pentru a servi străinii cumpărători cu un schimb valutar pe cinste. Numai că cinstea acestuia este adesea discutată pe la colturi de drum. Plătește-i cu aceiasi monedă!**
- flag: **ITEC{nu_umbl4_cu_0c4u4_m1c4}**
- deploy: `cd ~/path ; docker-compose up`

### Spânzurătoarea - FeDEX - done
- descriere: **Incepe ora de matematica, iar domnul profesor propune sa jucati jocul "spânzuratoarea". Insă regulile arată putin diferit: aveti o singura sansă să ghiciti intreg cuvantul, iar pentru fiecare literă există anumite constrangeri. Succes!**
- flag: **ITEC{tr41m_4l4tur1_d3_34_p4n4_mur1m_474rna71_d3_34}**
- deploy: `none`


# Reverse

### Fata Morgana - FeDEX - wip
- description: **Din departare se zareste un flag, dar cu cat te apropii mai mult de el, pare sa dispara.**
- flag: **ITEC{f4t4_m0rg4na_ba73_camp11_Cu_un_POKEMON}**
- deploy: `none`

### Challenge 2 - FeDEX - idea
- description: 
- flag: **ITEC{}**
- deploy: `none`

# Web

### Challange 1 - Paul - done
- descriere: Vacuta milka vrea sa vorbeasca cu tine.
- flag: **ITEC{V4CUTA_M1LKA_4_U1TAT_D3_INJ3CT4R3A_DE_C0M3NZ1}**
- will -> docker
### Challange 2 - Paul - done
- descriere: Acum s-a suparat si nu mai vrea sa raspuna la orice cuvant :(.
- flag: **ITEC{V4CUTA_M1LKA_4_C0M1S0_D1NOU}**
- will -> docker
### Challange 3 - Paul - done
- descriere **Lui Flamanzila ii plac foarte mult prajiturile. Daca ii dai ceea ce el vrea, o sa ti dea si el ceva in schimb.**
- flag: **ITEC{T1E_1T1_PL4C_PR1J1TURI1LE}**
- `cd ~/path ; docker-compose up`
### Challange 4 - Paul - idea
- XXE 

### Challange 5 - Paul & FeDEX - idea
- Web scraping 

# Pwn

### Păcală 2.0 - FeDEX - idea
- descriere: **Din cauza lockdown-ului, Pacala s-a digitalizat si pacaleste cetatenii pe internet. Incearca sa-l pacalesti si tu, hackuindu-i aplicatia de pacaleli.**
- flag: **ITEC{Pr0s7_73-4_m41_f4cu7_m4-74_PACALA!}**
- deploy: `cd ~/path ; docker-compose up`

### Tândală 2.0 - FeDEX - idea
- descriere: **Ca să nu se lase mai prejos, si Tândală si-a creat  propriul lui sistem informatic, insă acesta, lenes fiind, a folosit canary-ul default, nu si-a implementat unul custom. Dovedeste-i ca aceasta este o gresala!**
- flag: **ITEC{l3n3a_ES73_7e4m4_d3_munc4_c4r3_urm3Az4}**
- deploy: `cd ~/path ; docker-compose up`


### Ochilă 2.0 - Paul - done
- descriere: **Ochilă se laudă că securitatea lui este mai bună decat a amicilor săi, insă ii tot fug ochii cu mult dupa canary, oare ce s-ar putea găsi acolo?**
- flag: **ITEC{Ochila_frate_cu_Orbila_var_primar_cu_Chiorila}**
- deploy: `cd ~/path ; docker-compose up`


# Forensics

### Challange 1 - Paul - done
- descriere: **Dintr-o data am observat pe trafic mai multe request-uri DNS, ceea ce e putin suspect. Misiunea ta e sa afli ce a exfiltrat atacatorul.** 
- flag: **ITEC{Exf1ltr4r3a_Pr1n_Dns_Nu_E_S1lentio4sa}**
- Rezolvare: **tshark -r dns.pcap -T fields -e dns.qry.name  -Y  "dns.qry.name" | awk -F "." '{print $1}' | uniq | tr -d "\n" | xxd -r -p**

### Challange 2 - Paul - done 

- descriere: **Ochila s-a suparat de Setila, si vrea sa se conecteze la reteaua sa. A reusit sa captureze acest trafic, poti tu oare sa-l ajuti sa afle parola ?**
- flag: **ITEC{vrajitoarea}**

### Challange 3 - Paul - doen

- descriere: **Ochila a mai observat inca o data ceva ciudat, acum sunt multe packete de tip ICMP.Poti sa-l ajuti sa gaseasca ce se afla in ele?**
- flag **ITEC{P1NG_P0NG_PIN5_PON5_PING_PONGGG}**



# Misc

### Gheorghe cel voinic - FeDEX - done
- descriere: **După o noapte petrecută la pândă, Gheorghe zăreste hotul de mere. Urmăreste-l in prin labirint și il vei putea prinde la ultimul nivel.**
- flag: **ITEC{Și_încălecai_pe-o_căpșună_și_vă_spusei_o_minciună}**
- deploy: `cd ~/path ; docker-compose up`

### Format
- descriere: **Un fel de vacuta milka, doar ca nu asa fancy si fara vacuta :))**
- flag:  **ITEC{S4_NU_A1_1NCREDER3_1N_F0RM4T}**


### Arta
- descriere: **Se zice ca fiecare opera de arta transmite ceva. Ce iti transmite aceasta ? (este de origine olandeza)**
- flag: **ITEC{P1ET_M0NDR1AN_A_F0ST_UN_P1CT0R}**

# Stegano

### Poza Itec - Paul - done

- descriere: **Am primit aceasta poza. Presimt ca se ascunde ceva in ea, poti sa imi spui ce ?**
- flag: **ITEC{ST1AI_CA_P0T1_4SCUND3_F1S1ER3_4N_POZ3??!}**

### Apus in Timisoara - Paul - done

- descriere: **O poza minunata cu un apus in Timisoara. Sau e mai mult decat atat ?**
- flag: **ITEC{T1M1S04RA_3_FRUM0ASA_S1_UNIC4_NU_I_ASA??}**
