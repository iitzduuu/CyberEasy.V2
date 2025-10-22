rule CS_EASY {
    meta:
        autor = "Grupo de CYBER"
        descricao = "Achar malware" 
    strings: 
        $a = "malware"
    condition:
        $a
}