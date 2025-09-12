rule DetectaAmeaca : malware trojan spyware {

    meta:
autor = "Grupo de CYBER
        descricao = "Achar malware"
        data = "2025.08.29
        version = "1.0"

strings: 
$s1 = "malware"
$s2 = "trojan"
$s3 = "spyware"

condition:
        any of ($s*) or all of them
