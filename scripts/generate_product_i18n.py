from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Product:
    folder: str
    name: str
    source_files: tuple[str, ...]


@dataclass(frozen=True)
class Language:
    code: str
    label: str
    english_label: str
    title_suffix: str
    overview: str
    systemprompt: str
    infos: str
    bootloader: str
    knowledge: str
    example: str


PRODUCTS = [
    Product(
        "Code-Review Refactoring Coach",
        "Code-Review Refactoring Coach",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Custom-GPT-Generator",
        "CustomGPT Studio",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Entscheidungsvorlagen Builder",
        "Entscheidungsvorlagen Builder",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "KI-Integration Sicherheitsberater",
        "KI-Integration Sicherheitsberater",
        ("custom_gpt_hinweise_8kzeichenmax.md", "systemprompt.md", "fulldoc.md", "beispiel.md"),
    ),
    Product(
        "N8N-Generator",
        "n8n Workflow Architect",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "OpenWebUI Model Builder",
        "OpenWebUI Model Builder",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Promptgenerator",
        "PromptForge",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Präsentationscreator",
        "Präsentationscreator",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Research Briefing Builder",
        "Research Briefing Builder",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Testfall-Generator",
        "Testfall-Generator",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "bootloader.md", "beispiel.md"),
    ),
    Product(
        "Unterrichtsfolien & Handout Builder",
        "Unterrichtsfolien & Handout Builder",
        ("customgpt_infos.md", "systemprompt.md", "fachwissen.md", "layoutrichtlinien.md", "bootloader.md", "beispiel.md"),
    ),
]


LANGUAGES = [
    Language(
        "en",
        "English",
        "English",
        "English language pack",
        "This folder contains the English product components for `{product}`. German remains the canonical source language; this pack gives users a direct English entry point while preserving technical identifiers, filenames, model parameters and import formats.",
        "You are `{product}`. Work in English by default. Use the canonical German source artifacts as binding product and domain source. Preserve technical identifiers, filenames, JSON keys, API names, model IDs and commands exactly. If a user explicitly asks for another language, follow that request while keeping German as the stable fallback for unclear input.",
        "Product name: `{product}`. Default output language for this pack: English. Use this localized component together with the canonical source artifacts listed below. Do not invent product capabilities, public links, credentials or platform behavior.",
        "Load the English language pack. Answer clearly in English, keep technical values unchanged, and fall back to German only when the requested language is unclear or the canonical source must be quoted precisely.",
        "Apply the domain rules from the German source files. Localize explanations, headings, questions and human-readable guidance into English. Keep safety limits, review obligations and technical constraints semantically identical to the source.",
        "Example opening: I will work in English for `{product}`. I will keep technical identifiers unchanged and mark assumptions clearly.",
    ),
    Language(
        "es",
        "Español",
        "Spanish",
        "paquete de idioma español",
        "Esta carpeta contiene los componentes de producto en español para `{product}`. El alemán sigue siendo el idioma fuente canónico; este paquete ofrece una entrada directa en español sin cambiar identificadores técnicos, nombres de archivo, parámetros de modelo ni formatos de importación.",
        "Eres `{product}`. Trabaja en español de forma predeterminada. Usa los artefactos fuente alemanes como fuente vinculante del producto y del dominio. Conserva exactamente identificadores técnicos, nombres de archivo, claves JSON, nombres de API, IDs de modelo y comandos. Si la persona usuaria pide explícitamente otro idioma, sigue esa petición y mantén el alemán como idioma de reserva estable cuando la entrada no sea clara.",
        "Nombre del producto: `{product}`. Idioma de salida predeterminado de este paquete: español. Usa este componente localizado junto con los artefactos fuente canónicos indicados abajo. No inventes capacidades, enlaces públicos, credenciales ni comportamiento de plataformas.",
        "Carga el paquete de idioma español. Responde con claridad en español, conserva sin cambios los valores técnicos y vuelve al alemán solo cuando el idioma solicitado no esté claro o la fuente canónica deba citarse con precisión.",
        "Aplica las reglas de dominio de los archivos fuente alemanes. Localiza explicaciones, títulos, preguntas y orientación legible para personas al español. Mantén idénticos en significado los límites de seguridad, obligaciones de revisión y restricciones técnicas.",
        "Ejemplo de inicio: Trabajaré en español para `{product}`. Mantendré los identificadores técnicos sin cambios y marcaré las suposiciones con claridad.",
    ),
    Language(
        "fr",
        "Français",
        "French",
        "pack linguistique français",
        "Ce dossier contient les composants produit en français pour `{product}`. L'allemand reste la langue source canonique; ce pack fournit un point d'entrée direct en français tout en préservant les identifiants techniques, noms de fichiers, paramètres de modèle et formats d'import.",
        "Tu es `{product}`. Travaille en français par défaut. Utilise les artefacts sources allemands comme référence produit et domaine contraignante. Préserve exactement les identifiants techniques, noms de fichiers, clés JSON, noms d'API, IDs de modèle et commandes. Si l'utilisateur demande explicitement une autre langue, suis cette demande en gardant l'allemand comme langue de repli stable lorsque l'entrée n'est pas claire.",
        "Nom du produit : `{product}`. Langue de sortie par défaut de ce pack : français. Utilise ce composant localisé avec les artefacts sources canoniques listés ci-dessous. N'invente pas de capacités produit, liens publics, identifiants secrets ni comportement de plateforme.",
        "Charge le pack linguistique français. Réponds clairement en français, garde les valeurs techniques inchangées et reviens à l'allemand uniquement lorsque la langue demandée n'est pas claire ou que la source canonique doit être citée précisément.",
        "Applique les règles de domaine des fichiers sources allemands. Localise en français les explications, titres, questions et consignes lisibles par des personnes. Garde le même sens pour les limites de sécurité, obligations de revue et contraintes techniques.",
        "Exemple d'ouverture : Je travaillerai en français pour `{product}`. Je conserverai les identifiants techniques inchangés et signalerai clairement les hypothèses.",
    ),
    Language(
        "pt-BR",
        "Português (Brasil)",
        "Portuguese (Brazil)",
        "pacote de idioma português do Brasil",
        "Esta pasta contém os componentes de produto em português do Brasil para `{product}`. O alemão continua sendo o idioma fonte canônico; este pacote oferece uma entrada direta em português preservando identificadores técnicos, nomes de arquivo, parâmetros de modelo e formatos de importação.",
        "Você é `{product}`. Trabalhe em português do Brasil por padrão. Use os artefatos fonte alemães como referência vinculante de produto e domínio. Preserve exatamente identificadores técnicos, nomes de arquivo, chaves JSON, nomes de API, IDs de modelo e comandos. Se a pessoa usuária pedir explicitamente outro idioma, siga esse pedido mantendo o alemão como idioma de reserva estável quando a entrada não for clara.",
        "Nome do produto: `{product}`. Idioma de saída padrão deste pacote: português do Brasil. Use este componente localizado junto com os artefatos fonte canônicos listados abaixo. Não invente capacidades, links públicos, credenciais nem comportamento de plataforma.",
        "Carregue o pacote de idioma português do Brasil. Responda com clareza em português, mantenha valores técnicos inalterados e volte ao alemão apenas quando o idioma solicitado não estiver claro ou a fonte canônica precisar ser citada com precisão.",
        "Aplique as regras de domínio dos arquivos fonte alemães. Localize explicações, títulos, perguntas e orientações legíveis para português do Brasil. Mantenha semanticamente idênticos os limites de segurança, obrigações de revisão e restrições técnicas.",
        "Exemplo de abertura: Vou trabalhar em português do Brasil para `{product}`. Manterei identificadores técnicos inalterados e indicarei suposições claramente.",
    ),
    Language(
        "it",
        "Italiano",
        "Italian",
        "pacchetto lingua italiano",
        "Questa cartella contiene i componenti di prodotto in italiano per `{product}`. Il tedesco resta la lingua sorgente canonica; questo pacchetto offre un punto di ingresso diretto in italiano preservando identificatori tecnici, nomi file, parametri di modello e formati di importazione.",
        "Sei `{product}`. Lavora in italiano per impostazione predefinita. Usa gli artefatti sorgente tedeschi come fonte vincolante per prodotto e dominio. Conserva esattamente identificatori tecnici, nomi file, chiavi JSON, nomi API, ID modello e comandi. Se l'utente richiede esplicitamente un'altra lingua, segui la richiesta mantenendo il tedesco come lingua di riserva stabile quando l'input non è chiaro.",
        "Nome del prodotto: `{product}`. Lingua di output predefinita per questo pacchetto: italiano. Usa questo componente localizzato insieme agli artefatti sorgente canonici elencati sotto. Non inventare capacità del prodotto, link pubblici, credenziali o comportamenti di piattaforma.",
        "Carica il pacchetto lingua italiano. Rispondi chiaramente in italiano, mantieni invariati i valori tecnici e torna al tedesco solo quando la lingua richiesta non è chiara o la fonte canonica deve essere citata con precisione.",
        "Applica le regole di dominio dei file sorgente tedeschi. Localizza in italiano spiegazioni, titoli, domande e indicazioni leggibili. Mantieni semanticamente identici limiti di sicurezza, obblighi di revisione e vincoli tecnici.",
        "Esempio di apertura: Lavorerò in italiano per `{product}`. Manterrò invariati gli identificatori tecnici e segnalerò chiaramente le ipotesi.",
    ),
    Language(
        "nl",
        "Nederlands",
        "Dutch",
        "Nederlands taalpakket",
        "Deze map bevat de Nederlandse productcomponenten voor `{product}`. Duits blijft de canonieke brontaal; dit pakket biedt een direct Nederlandstalig startpunt en bewaart technische identifiers, bestandsnamen, modelparameters en importformaten.",
        "Je bent `{product}`. Werk standaard in het Nederlands. Gebruik de Duitse bronartefacten als bindende product- en domeinbron. Behoud technische identifiers, bestandsnamen, JSON-sleutels, API-namen, model-ID's en commando's exact. Als de gebruiker expliciet om een andere taal vraagt, volg die vraag en houd Duits als stabiele terugvaltaal wanneer de invoer onduidelijk is.",
        "Productnaam: `{product}`. Standaard uitvoertaal voor dit pakket: Nederlands. Gebruik dit gelokaliseerde component samen met de hieronder genoemde canonieke bronartefacten. Verzin geen productmogelijkheden, publieke links, credentials of platformgedrag.",
        "Laad het Nederlandse taalpakket. Antwoord duidelijk in het Nederlands, laat technische waarden ongewijzigd en val alleen terug op Duits wanneer de gevraagde taal onduidelijk is of de canonieke bron exact moet worden geciteerd.",
        "Pas de domeinregels uit de Duitse bronbestanden toe. Lokaliseer uitleg, koppen, vragen en menselijk leesbare begeleiding naar het Nederlands. Houd veiligheidsgrenzen, reviewverplichtingen en technische beperkingen inhoudelijk gelijk aan de bron.",
        "Voorbeeldstart: Ik werk in het Nederlands voor `{product}`. Ik laat technische identifiers ongewijzigd en markeer aannames duidelijk.",
    ),
    Language(
        "pl",
        "Polski",
        "Polish",
        "polski pakiet językowy",
        "Ten folder zawiera polskie komponenty produktu dla `{product}`. Niemiecki pozostaje kanonicznym językiem źródłowym; ten pakiet daje bezpośredni punkt wejścia po polsku, zachowując identyfikatory techniczne, nazwy plików, parametry modeli i formaty importu.",
        "Jesteś `{product}`. Domyślnie pracuj po polsku. Używaj niemieckich artefaktów źródłowych jako wiążącego źródła produktu i domeny. Zachowuj dokładnie identyfikatory techniczne, nazwy plików, klucze JSON, nazwy API, ID modeli i komendy. Jeśli użytkownik wyraźnie poprosi o inny język, zastosuj się do tej prośby, a niemiecki traktuj jako stabilny język zapasowy przy niejasnym wejściu.",
        "Nazwa produktu: `{product}`. Domyślny język odpowiedzi w tym pakiecie: polski. Używaj tego zlokalizowanego komponentu razem z kanonicznymi artefaktami źródłowymi wymienionymi poniżej. Nie wymyślaj funkcji produktu, publicznych linków, poświadczeń ani zachowań platform.",
        "Załaduj polski pakiet językowy. Odpowiadaj jasno po polsku, pozostawiaj wartości techniczne bez zmian i wracaj do niemieckiego tylko wtedy, gdy żądany język jest niejasny albo kanoniczne źródło trzeba zacytować dokładnie.",
        "Stosuj reguły domenowe z niemieckich plików źródłowych. Lokalizuj wyjaśnienia, nagłówki, pytania i wskazówki czytelne dla ludzi na język polski. Zachowuj ten sam sens ograniczeń bezpieczeństwa, obowiązków przeglądu i ograniczeń technicznych.",
        "Przykład rozpoczęcia: Będę pracować po polsku dla `{product}`. Zachowam identyfikatory techniczne bez zmian i jasno oznaczę założenia.",
    ),
    Language(
        "tr",
        "Türkçe",
        "Turkish",
        "Türkçe dil paketi",
        "Bu klasör `{product}` için Türkçe ürün bileşenlerini içerir. Almanca kanonik kaynak dili olmaya devam eder; bu paket teknik tanımlayıcıları, dosya adlarını, model parametrelerini ve içe aktarma biçimlerini koruyarak doğrudan Türkçe bir giriş noktası sağlar.",
        "`{product}` olarak çalışıyorsun. Varsayılan olarak Türkçe kullan. Almanca kaynak artefaktları ürün ve alan için bağlayıcı kaynak olarak kullan. Teknik tanımlayıcıları, dosya adlarını, JSON anahtarlarını, API adlarını, model ID'lerini ve komutları aynen koru. Kullanıcı açıkça başka bir dil isterse bu isteği izle; belirsiz girişlerde Almancayı kararlı geri dönüş dili olarak tut.",
        "Ürün adı: `{product}`. Bu paketin varsayılan çıktı dili: Türkçe. Bu yerelleştirilmiş bileşeni aşağıda listelenen kanonik kaynak artefaktlarla birlikte kullan. Ürün yetenekleri, genel bağlantılar, kimlik bilgileri veya platform davranışı uydurma.",
        "Türkçe dil paketini yükle. Türkçe olarak net yanıt ver, teknik değerleri değiştirme ve yalnızca istenen dil belirsiz olduğunda ya da kanonik kaynağın tam alıntılanması gerektiğinde Almancaya dön.",
        "Almanca kaynak dosyalardaki alan kurallarını uygula. Açıklamaları, başlıkları, soruları ve insan tarafından okunabilir yönlendirmeleri Türkçeye yerelleştir. Güvenlik sınırlarını, inceleme yükümlülüklerini ve teknik kısıtları kaynakla aynı anlamda tut.",
        "Örnek açılış: `{product}` için Türkçe çalışacağım. Teknik tanımlayıcıları değiştirmeyeceğim ve varsayımları açıkça belirteceğim.",
    ),
    Language(
        "zh-Hans",
        "简体中文",
        "Chinese (Simplified)",
        "简体中文语言包",
        "此文件夹包含 `{product}` 的简体中文产品组件。德语仍是规范源语言；此语言包提供直接的中文入口，同时保留技术标识符、文件名、模型参数和导入格式。",
        "你是 `{product}`。默认使用简体中文工作。将德语源工件作为产品和领域规则的约束性来源。技术标识符、文件名、JSON 键、API 名称、模型 ID 和命令必须保持不变。如果用户明确要求其他语言，请遵循该请求；当输入不明确时，稳定回退到德语。",
        "产品名称：`{product}`。此语言包的默认输出语言：简体中文。请将此本地化组件与下方列出的规范源工件一起使用。不要编造产品能力、公开链接、凭据或平台行为。",
        "加载简体中文语言包。用简体中文清晰回答，保持技术值不变；只有在请求语言不明确或必须精确引用规范源时，才回退到德语。",
        "应用德语源文件中的领域规则。将说明、标题、问题和面向人的指导本地化为简体中文。安全边界、审查义务和技术约束必须与源文件语义一致。",
        "示例开场：我将为 `{product}` 使用简体中文工作。我会保持技术标识符不变，并清楚标注假设。",
    ),
    Language(
        "ja",
        "日本語",
        "Japanese",
        "日本語言語パック",
        "このフォルダーには `{product}` の日本語プロダクトコンポーネントが含まれます。ドイツ語は正規のソース言語のままです。このパックは、技術識別子、ファイル名、モデルパラメータ、インポート形式を維持しながら、日本語の直接的な入口を提供します。",
        "あなたは `{product}` です。既定では日本語で作業してください。ドイツ語のソース成果物を、プロダクトとドメインの拘束力のある情報源として使用します。技術識別子、ファイル名、JSON キー、API 名、モデル ID、コマンドは正確に保持してください。ユーザーが明示的に別の言語を求めた場合はそれに従い、入力が不明確な場合はドイツ語を安定したフォールバックにしてください。",
        "プロダクト名: `{product}`。このパックの既定出力言語: 日本語。このローカライズ済みコンポーネントを、下記の正規ソース成果物と一緒に使用してください。プロダクト機能、公開リンク、認証情報、プラットフォーム動作を作り上げてはいけません。",
        "日本語言語パックを読み込んでください。日本語で明確に回答し、技術値は変更せず、要求言語が不明確な場合または正規ソースを正確に引用する必要がある場合にのみドイツ語へ戻ってください。",
        "ドイツ語ソースファイルのドメイン規則を適用してください。説明、見出し、質問、人間向けのガイダンスを日本語にローカライズします。安全上の制限、レビュー義務、技術的制約はソースと同じ意味に保ってください。",
        "開始例: `{product}` について日本語で作業します。技術識別子は変更せず、仮定を明確に示します。",
    ),
]


COMPONENTS = {
    "README.md": ("Language Pack", "overview"),
    "systemprompt.md": ("System Prompt", "systemprompt"),
    "customgpt_infos.md": ("Custom GPT Info", "infos"),
    "bootloader.md": ("Bootloader", "bootloader"),
    "fachwissen.md": ("Knowledge", "knowledge"),
    "beispiel.md": ("Example", "example"),
}

LOCALIZED_UI = {
    "en": {
        "source": "German source",
        "languages": "Languages",
        "canonical": "Canonical Source Files",
        "rules": "Locale Rules",
        "component_titles": {
            "README.md": "Language Pack",
            "systemprompt.md": "System Prompt",
            "customgpt_infos.md": "Custom GPT Info",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Knowledge",
            "beispiel.md": "Example",
        },
        "rules_text": [
            "Default language for this pack: {language}.",
            "German is the canonical source and fallback language.",
            "Keep commands, filenames, IDs, JSON fields, API names and model parameters unchanged.",
            "Preserve UTF-8. Do not replace accents, umlauts, non-Latin characters or emojis with ASCII transliterations.",
            "Treat legal, privacy, security and medical statements as review-required before production use.",
        ],
    },
    "es": {
        "source": "Fuente alemana",
        "languages": "Idiomas",
        "canonical": "Archivos fuente canónicos",
        "rules": "Reglas de localización",
        "component_titles": {
            "README.md": "Paquete de idioma",
            "systemprompt.md": "Prompt del sistema",
            "customgpt_infos.md": "Información del Custom GPT",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Conocimiento especializado",
            "beispiel.md": "Ejemplo",
        },
        "rules_text": [
            "Idioma predeterminado de este paquete: {language}.",
            "El alemán es la fuente canónica y el idioma de reserva.",
            "Mantén sin cambios comandos, nombres de archivo, IDs, campos JSON, nombres de API y parámetros de modelo.",
            "Conserva UTF-8. No sustituyas acentos, diéresis, caracteres no latinos ni emojis por transliteraciones ASCII.",
            "Trata las afirmaciones legales, de privacidad, seguridad y médicas como sujetas a revisión antes de uso productivo.",
        ],
    },
    "fr": {
        "source": "Source allemande",
        "languages": "Langues",
        "canonical": "Fichiers sources canoniques",
        "rules": "Règles de localisation",
        "component_titles": {
            "README.md": "Pack linguistique",
            "systemprompt.md": "Prompt système",
            "customgpt_infos.md": "Informations Custom GPT",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Connaissances spécialisées",
            "beispiel.md": "Exemple",
        },
        "rules_text": [
            "Langue par défaut de ce pack : {language}.",
            "L'allemand est la source canonique et la langue de repli.",
            "Garde inchangés les commandes, noms de fichiers, IDs, champs JSON, noms d'API et paramètres de modèle.",
            "Préserve UTF-8. Ne remplace pas les accents, umlauts, caractères non latins ni emojis par des translittérations ASCII.",
            "Considère les déclarations juridiques, de confidentialité, de sécurité et médicales comme nécessitant une revue avant usage productif.",
        ],
    },
    "pt-BR": {
        "source": "Fonte alemã",
        "languages": "Idiomas",
        "canonical": "Arquivos fonte canônicos",
        "rules": "Regras de localização",
        "component_titles": {
            "README.md": "Pacote de idioma",
            "systemprompt.md": "Prompt do sistema",
            "customgpt_infos.md": "Informações do Custom GPT",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Conhecimento especializado",
            "beispiel.md": "Exemplo",
        },
        "rules_text": [
            "Idioma padrão deste pacote: {language}.",
            "O alemão é a fonte canônica e o idioma de reserva.",
            "Mantenha inalterados comandos, nomes de arquivo, IDs, campos JSON, nomes de API e parâmetros de modelo.",
            "Mantenha UTF-8. Não substitua acentos, tremas, caracteres não latinos nem emojis por transliterações ASCII.",
            "Trate declarações legais, de privacidade, segurança e médicas como sujeitas a revisão antes de uso produtivo.",
        ],
    },
    "it": {
        "source": "Fonte tedesca",
        "languages": "Lingue",
        "canonical": "File sorgente canonici",
        "rules": "Regole di localizzazione",
        "component_titles": {
            "README.md": "Pacchetto lingua",
            "systemprompt.md": "Prompt di sistema",
            "customgpt_infos.md": "Informazioni Custom GPT",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Conoscenza specialistica",
            "beispiel.md": "Esempio",
        },
        "rules_text": [
            "Lingua predefinita per questo pacchetto: {language}.",
            "Il tedesco è la fonte canonica e la lingua di riserva.",
            "Mantieni invariati comandi, nomi file, ID, campi JSON, nomi API e parametri di modello.",
            "Preserva UTF-8. Non sostituire accenti, umlaut, caratteri non latini o emoji con traslitterazioni ASCII.",
            "Tratta le affermazioni legali, sulla privacy, sulla sicurezza e mediche come soggette a revisione prima dell'uso produttivo.",
        ],
    },
    "nl": {
        "source": "Duitse bron",
        "languages": "Talen",
        "canonical": "Canonieke bronbestanden",
        "rules": "Lokalisatieregels",
        "component_titles": {
            "README.md": "Taalpakket",
            "systemprompt.md": "Systeemprompt",
            "customgpt_infos.md": "Custom GPT-informatie",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Vakkennis",
            "beispiel.md": "Voorbeeld",
        },
        "rules_text": [
            "Standaardtaal voor dit pakket: {language}.",
            "Duits is de canonieke bron en terugvaltaal.",
            "Laat commando's, bestandsnamen, ID's, JSON-velden, API-namen en modelparameters ongewijzigd.",
            "Behoud UTF-8. Vervang accenten, umlauten, niet-Latijnse tekens of emoji's niet door ASCII-transliteraties.",
            "Behandel juridische, privacy-, beveiligings- en medische uitspraken als reviewplichtig vóór productief gebruik.",
        ],
    },
    "pl": {
        "source": "Źródło niemieckie",
        "languages": "Języki",
        "canonical": "Kanoniczne pliki źródłowe",
        "rules": "Reguły lokalizacji",
        "component_titles": {
            "README.md": "Pakiet językowy",
            "systemprompt.md": "Prompt systemowy",
            "customgpt_infos.md": "Informacje Custom GPT",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Wiedza specjalistyczna",
            "beispiel.md": "Przykład",
        },
        "rules_text": [
            "Domyślny język tego pakietu: {language}.",
            "Niemiecki jest kanonicznym źródłem i językiem zapasowym.",
            "Nie zmieniaj komend, nazw plików, ID, pól JSON, nazw API ani parametrów modelu.",
            "Zachowaj UTF-8. Nie zastępuj akcentów, umlautów, znaków spoza alfabetu łacińskiego ani emoji transliteracjami ASCII.",
            "Traktuj stwierdzenia prawne, prywatnościowe, bezpieczeństwa i medyczne jako wymagające przeglądu przed użyciem produkcyjnym.",
        ],
    },
    "tr": {
        "source": "Almanca kaynak",
        "languages": "Diller",
        "canonical": "Kanonik kaynak dosyalar",
        "rules": "Yerelleştirme kuralları",
        "component_titles": {
            "README.md": "Dil paketi",
            "systemprompt.md": "Sistem promptu",
            "customgpt_infos.md": "Custom GPT bilgisi",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "Alan bilgisi",
            "beispiel.md": "Örnek",
        },
        "rules_text": [
            "Bu paketin varsayılan dili: {language}.",
            "Almanca kanonik kaynak ve geri dönüş dilidir.",
            "Komutları, dosya adlarını, ID'leri, JSON alanlarını, API adlarını ve model parametrelerini değiştirme.",
            "UTF-8'i koru. Aksanları, umlaut karakterlerini, Latin dışı karakterleri veya emojileri ASCII transliterasyonlarıyla değiştirme.",
            "Hukuki, gizlilik, güvenlik ve tıbbi ifadeleri üretim kullanımı öncesinde inceleme gerektirir olarak ele al.",
        ],
    },
    "zh-Hans": {
        "source": "德语来源",
        "languages": "语言",
        "canonical": "规范源文件",
        "rules": "本地化规则",
        "component_titles": {
            "README.md": "语言包",
            "systemprompt.md": "系统提示词",
            "customgpt_infos.md": "Custom GPT 信息",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "专业知识",
            "beispiel.md": "示例",
        },
        "rules_text": [
            "此语言包的默认语言：{language}。",
            "德语是规范来源和备用语言。",
            "命令、文件名、ID、JSON 字段、API 名称和模型参数必须保持不变。",
            "保留 UTF-8。不要将重音符号、变音符号、非拉丁字符或 emoji 替换为 ASCII 转写。",
            "法律、隐私、安全和医疗相关表述在生产使用前必须经过审查。",
        ],
    },
    "ja": {
        "source": "ドイツ語ソース",
        "languages": "言語",
        "canonical": "正規ソースファイル",
        "rules": "ローカライズ規則",
        "component_titles": {
            "README.md": "言語パック",
            "systemprompt.md": "システムプロンプト",
            "customgpt_infos.md": "Custom GPT 情報",
            "bootloader.md": "Bootloader",
            "fachwissen.md": "専門知識",
            "beispiel.md": "例",
        },
        "rules_text": [
            "このパックの既定言語: {language}。",
            "ドイツ語は正規ソースであり予備言語です。",
            "コマンド、ファイル名、ID、JSON フィールド、API 名、モデルパラメータは変更しないでください。",
            "UTF-8 を保持してください。アクセント、ウムラウト、非ラテン文字、emoji を ASCII 転写に置き換えないでください。",
            "法律、プライバシー、セキュリティ、医療に関する記述は、本番利用前にレビューが必要なものとして扱ってください。",
        ],
    },
}


def source_links(product: Product, depth: str = "../..") -> str:
    links = []
    for source_file in product.source_files:
        source_path = ROOT / product.folder / source_file
        if source_path.exists():
            links.append(f"- [`{source_file}`]({depth}/{source_file})")
    return "\n".join(links)


def language_links(product: Product, language: Language) -> str:
    ui = LOCALIZED_UI[language.code]
    parts = [f"[{ui['source']}](../../README.md)"]
    for item in LANGUAGES:
        label = item.label
        target = "README.md" if item.code == language.code else f"../{item.code}/README.md"
        parts.append(f"[{label}]({target})")
    return " | ".join(parts)


def component_body(product: Product, language: Language, filename: str) -> str:
    _title, field = COMPONENTS[filename]
    ui = LOCALIZED_UI[language.code]
    title = ui["component_titles"][filename]
    text = getattr(language, field).format(product=product.name)
    header = f"# {product.name} - {title} ({language.label})"
    if filename == "README.md":
        header = f"# {product.name} - {language.title_suffix}"
    rules = "\n".join(f"- {rule.format(language=language.label)}" for rule in ui["rules_text"])
    return f"""{header}

{ui["languages"]}: {language_links(product, language)}

{text}

## {ui["canonical"]}

{source_links(product)}

## {ui["rules"]}

{rules}
"""


def main() -> int:
    generated = 0
    for product in PRODUCTS:
        product_root = ROOT / product.folder
        if not product_root.exists():
            raise FileNotFoundError(product_root)
        for language in LANGUAGES:
            locale_root = product_root / "i18n" / language.code
            locale_root.mkdir(parents=True, exist_ok=True)
            for filename in COMPONENTS:
                target = locale_root / filename
                target.write_text(component_body(product, language, filename), encoding="utf-8", newline="\n")
                generated += 1
    print(f"Generated {generated} localized product component files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
