from sistem.sahne_yazici import sahne

def saldir():
    sahne([
        "💥 KodKalkanı saldırıyor!",
        "🔍 Güvenlik açıklarını analiz ediyor...",
        "🛡️ Ağ trafiğine zararlı kod enjekte etmeye çalışıyor...",
    ], renk='red')

def savun():
    sahne([
        "🛡️ KodKalkanı savunma moduna geçti!",
        "🔐 Güvenlik duvarı aktif!",
        "📊 Gelişmiş tehdit algılama devrede...",
    ], renk='green')
