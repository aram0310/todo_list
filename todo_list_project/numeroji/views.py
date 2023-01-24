from django.shortcuts import render
from deep_translator import GoogleTranslator
from  django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
import time
from . models import Names; 

def home(request):
       
    original_text = translated = ''
    if request.method == "POST":
        name = request.POST['fullname']
        
        name_ob = Names(name=name)
        name_ob.save()
        
        name_weight = process_name(name)
        original_text, translated =  translate(name_weight)
        
    context = {
        'original' : original_text, 
        'translated': translated
        
    }
    
    return render(request, 'numeroji/home.html', context)

@csrf_exempt
def process_name_api(request):
    
    if request.method == 'GET':
        return HttpResponse({"data":"data "})
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        print(data.get('name'))
        
        name_ob = Names(name=data.get('name'))
        name_ob.save()
        
        name_weight = process_name(data.get('name'))
        original_text, translated =  translate(name_weight)
        
        result = {
            'original' : original_text, 
            'translated': translated
        
         }
        
        return JsonResponse(result)
    


q = {
    
    1: """
    Kader sayınız 1 ise bu hayata liderlik özelliklerinizi kullanmak için gelmiş bulunmaktasınız. \n
    
    Yaratıcı ve orijinal bir insansınız. Fikirlerinizi kolaylıkla eyleme dönüştürebiliyorsunuz. Siz bu dünyanın "uygulayıcı"larındansınız. \n
    
    Doğuştan gelen liderlik özelliklerinizden dolayı risk almak sizin grubunuzdakiler için sağlıklıdır. Ancak risk alma bağımlısı olmamaya dikkat etmelisiniz. Unutmayın ki sahip olduğunuz güce karşı sorumlusunuz.\n
   
    Kader sayısı 1 olanlar arasından bolca işadamları, işkadınları ve girişimciler çıkar. Bunun nedeni sahip olduğunuz olağanüstü kararlılık ve tutkulu doğanızdır. Kendinize olan güveniniz sayesinde hayat boyu sürecek iş ilişkileri kurarsınız. \n
   
    Sosyal anlamda veya iş anlamında geri kaldığınızı hissettiğiniz takdirde sabırsızlıklarınız su yüzüne çıkmaya başlayabilir. Bu da işleri fazlasıyla aceleye getirmenize, dolayısıyla önemli detayları gözden kaçırmanıza neden olabilir. Başarınız için bu eğiliminize her zaman dikkat etmelisiniz. \n
   
    1 yaratıcı gücü nedeniyle yoğun enerji içeren bir rakamdır. Bu nedenle kader sayısı 1 olanlar agresyon ve bağımlılık eğilimlerini kontrol altına alabildiklerinde liderlik özellikleri parlamaya başlar. Güçlü ve ilham verici kişiliğinizi dominant eğilimlerinizle gölgelemeyin. Başkalarının görüşlerine karşı anlayışlı ve sabırlı olmayı öğrenip güçlü doğanızı kontrollü bir yaratıcılıkla ifade edebildiğinizde hem iş hem de sosyal hayatınızın başarı kapıları ardına kadar açık olacaktır.
   
    """,
    
    2: """
    
    Kader sayınız 2 ise, bu hayata diplomasi ve barış yapıcı özelliklerinizi kullanmak için gelmiş bulunmaktasınız. \n
    
    2'ler bu dünyanın "arabulucu"larıdır. Bu nedenle bireysel çalışmalardan çok grup çalışmalarını tercih etmelidirler, çünkü doğuştan gelen özellikleri en iyi grup ortamlarında parlar. \n
    
    Siz kralın danışmanısınız. Perde arkasından yönetmekte ustalaşmışsınızdır. Grubun vazgeçilmezisiniz. Takım lideri pozisyonunda veya kilit noktadaki görevlerden birini üstlenmek kaydıyla iş dünyasında çok iyi para kazanabilirsiniz. Doğuştan problem çözme yeteneğine sahipsiniz, bu nedenle de işinizde çok kolay yükselirsiniz. 
    \n
    Nezaketiniz ve diplomasi yeteneğiniz size birçok dost kazandırır. Buna zaman zaman siz de şaşırsanız dahi çok popülersiniz. Alçakgönüllülüğünüz sayesinde daima takdir edilirsiniz. Çorbada tuzu olan herkesin katkısını görür, hakkını yemezsiniz. Biraz utangaçsınız ve herkesi memnun etmek istiyorsunuz. Verici doğanızı dengeleyip başkalarının sizden yararlanmasına izin vermediğiniz sürece başarılı olursunuz. Zaman zaman kendinize haksızlık edildiğini düşünebilirsiniz. Böyle bir durumda kalırsanız iki şeye bakmalısınız: Aşırı mı verici davrandınız, yoksa haklarınızı korumanız gereken yerde çekingen mi kaldınız? Sınırlarınızı çizmekten korkmayın,
    \n
    Biraz utangaçsınız ve herkesi memnun etmek istiyorsunuz. Verici doğanızı dengeleyip başkalarının sizden yararlanmasına izin vermediğiniz sürece başarılı olursunuz. Zaman zaman kendinize haksızlık edildiğini düşünebilirsiniz. Böyle bir durumda kalırsanız iki şeye bakmalısınız: Aşırı mı verici davrandınız, yoksa haklarınızı korumanız gereken yerde çekingen mi kaldınız? Sınırlarınızı çizmekten korkmayın, başarının anahtarını burada bulacaksınız. Ayrıca o kadar çok seveniniz var ki, bir sorunla karşılaştığınızda etrafınızda size destek olacak birileri mutlaka olacaktır.
    
    """,
    
    3: """ 
        Kader sayınız 3 ise, bu hayata ikna yeteneklerinizi ve yaratıcı özelliklerinizi kullanarak başkalarına ilham vermek için gelmiş bulunmaktasınız.
        \n
        Yazma, konuşma, müzik, oyunculuk, tasarımcılık ve öğretmenlik alanlarında son derece yeteneklisiniz. Eğlenceyi sever, görünüşünüz ve ses tonunuzla insanları etkilersiniz.
        \n
        Siz bu dünyanın "optimist"lerindensiniz. Herkesteki doğal yeteneği ve potansiyeli görebilme yeteneğiniz sayesinde etrafınızdakileri motive edersiniz. Sözleriniz ve fikirleriniz başkaları için ilham kaynağıdır.
    \n
        Bu hayattaki amacınız, insanların içlerindeki neşeyle temas kurmalarını sağlamak ve yeteneklerini keşfedip hayata geçirme konusunda onlara yardımcı olmayı da içerir. İyimser bakışınızdan ve ilham dolu sözlerinizden etkilenmemek mümkün değildir. Bu nedenle başkalarına hayat aşıladıkça siz de hayatla daha çok bütünleştiğinizi hissedeceksiniz.
\n
        3'ler bazen sığ ve yüzeysel olma eğilimi gösterebilirler. Başarılı olmak için dedikodu yapmaktan ve olayları gereksiz yere büyütmekten özellikle kaçınmanız gerekmektedir. Sıkılganlığınızı kontol altında tutmalısınız çünkü sizi negatife çeken şey budur. Bu nedenle yaratıcılığınızı kullanmak sizin için büyük önem taşımaktadır. Bunun için de kendinizi disiplin etmeye gönüllü olmalısınız çünkü önü kesilmiş ifade hayatla olan bağınızı koparıp canlılığınızı gölgeler. Sorunlar yerine sahip olduklarınıza odaklanır ve yaratıcı enerjinizi kullanırsanız, neşeniz hem kendi hayatınızı hem de başkalarınınkini aydınlatacaktır.
    
    """,
    
    4: """ 
        Kader sayınız 4 ise, bu hayata istikrarlı olmak ve organizasyon yeteneklerinizi kullanmak için gelmiş bulunmaktasınız.
        \n
        4'ler kendilerini en iyi iş alanında ifade ederler. İdarecilik becerileri son derece gelişmiştir. Proje yönetimi ve organizasyon içeren her türlü alanda başarılı olurlar. Sistematik ve düzenli doğaları sayesinde bir işi bitirmede üstün sabır göstermekten ve uzun saatler boyunca çalışmaktan kaçınmazlar. Bu da üstleri tarafından takdir görmelerini sağlar.
           \n
        Siz bu dünyanın "düzenleyici"lerindensiniz. Ayrıca ellerinizi kullanmada üstünüze yoktur. Çok iyi birer cerrah, mimar, mühendis, müzisyen ve öğretmen olabilirsiniz. Pratiksiniz ve çok tertiplisiniz. Aklınıza bir iş koydunuz mu, onu bitirene kadar istikrarlı bir biçimde yorulmadan çalışırsınız.
    \n
        Kader sayısı 4 olanların bilmeleri gereken şey bu dünyaya çalışmak için gelmiş olmalarıdır. Buradaki anahtar kelime "emek"tir. Merak etmeyin, emek verdiğiniz sürece evren çalışmalarınızı ödüllendirecektir. Azminiz ve istikrarlı çalışmanız sayesinde koşullarınız, ortamınız her ne olursa olsun emeklerinizin karşılığını alacaksınız. Ancak güvenlik duygusunu abartmaktan kaçınmalısınız.
       \n
        Vizyonunuzu her zaman geniş tutun çünkü katı ve esnek olmayan bir yaklaşıma sahip olma eğilimdesiniz. Hayat sadece siyah ve beyazdan ibaret değildir. Kendinizi biraz daha serbest bıraktığınızda, hayatın tüm renkleri yaşamınıza dolacak ve size arzu ettiğiniz bolluğun kapılarını açacaktır. Aşırı ciddiyetiniz ilişkilerinize zarar verebilir. Sadece sizin tercihleriniz üzerinden yaşanan bir ilişkinin size de mutluluk getirmediğini göreceksiniz. Bu nedenle toleranslı, sabırlı ve esnemeye gönüllü davranırsanız ilişkilerinizde özlemini duyduğunuz doyumu, eşitlik ve paylaşım duygusu yaşayacaksınız.
    """, 
    
    5: """ 
    
        Kader sayınız 5 ise, bu hayata özgürlük duygunuzu ifade etmek ve hayat yolunuzdaki değişimleri kucaklamak için gelmiş bulunmaktasınız.
        \n
        Çok yönlü 5'ler birçok yetenekle donanmış olarak hayata gelmişlerdir. Her alandaki becerileriyle hayranlık uyandırırlar. Son derece esnek olan bu bireyler her ortama kolaylıkla uyum sağlar. Pekçok mucit bu rakamdan çıkar. Yenilikçi ve maceracı doğaları onlara birçok kapının kolayca açılmasını sağlar.
            \n
        Siz bu dünyanın "özgür ruh"larındansınız. Zekanız ve çekiciliğiniz sayesinde sosyal çevrelerde de oldukça popülersiniz. Satış ve pazarlama becerileriniz de oldukça yüksektir. Deyim yerindeyse Eskimolar'a bile buz satarsınız! Gözlem yeteneğiniz sayesinde iyi birer stand-up'çı dahi olabilirsiniz. Risk almayı seversiniz. Kendi işinizin sahibi olmaktan ya da serbest çalışmaktan mutluluk duyarsınız.
        \n
        Kader sayısı 5 olanlar yaratıcıklarının ve ifadelerinin önünü kesen işlerde kendilerini hapsolmuş hissettiklerinden tekdüze işlerde çok mutsuz olurlar. Bu nedenle işlerini yeteneklerini kullanabilecekleri bir alandan seçmeleri çok önemlidir.
   \n
        Bazen değişim sizi ürkütebilir, çünkü sorumluluk almak istemeyebilirsiniz. Ancak sorumluluk almaz ve değişimi kucaklamazsanız hayatınızda gelişimin de olamayacağını anlamalısınız. Yanlış anlaşılmamak için boşboğazlık etme eğiliminizi de kontrol altına almalı, neyi kiminle paylaşacağınız konusunda daha dikkatli olmalısınız.
   \n
        Çabuk kavrayan yapınız nedeniyle çabuk da sıkılırsınız. Bu nedenle uzun süre aynı işi    yapma ya da kariyerinizi istikrarlı bir şekilde sürdürme konusunda ciddi problemler yaşabilirsiniz. Bu eğiliminiz eğitim hayatınız için de bir risk teşkil etmektedir.  Başarınızın anahtarı bir işi tamamlamadan diğerine başlamamakta yatmaktadır.
   \n
        Özgürlüğü seversiniz, ancak unutmayın ki disiplin içermeyen bir özgürlük uzun   vadede onu kaybetmenize dahi neden olabilir.
   
    """,
    
    6: 
        """ 
        Kader sayınız 6 ise, bu hayata başkalarına yardım etmek, yaşamlarımıza denge ve uyum getirmek için gelmiş bulunmaktasınız.
        \n
        6'lar doktor, hemşire, hasta bakıcı, psikolog, danışman, şifacı, öğretmen ve hayırseverlerdir. İnsanlar birine ihtiyaç duyduklarında başlarını 6'ların omuzlarına yaslar. 6'ların sevgi dolu ve gözeten doğaları onların Kozmik Anne ya da Kozmik Baba olarak adlandırılmalarına neden olmuştur.
       \n
        Siz bu dünyanın "denge kurucu"larındansınız. Herkesin yardımına koşar, sorumluluk almaktan kaçınmazsınız. Onları zor zamanlarında içinde bulundukları negatif ortamdan çekip çıkartmada ustasınızdır. İnsanları motive eder, sözlerinizle onları yüreklendirirsiniz.
            \n  
        Güzellik sizin için çok önemlidir. Estetik duygunuz gelişmiştir. Sanat, müzik ve edebiyat alanlarında da çok yeteneklisinizdir. Bulunduğunuz ortama denge getirir, uyumsuzluk ve karmaşadan hoşlanmazsınız. Ancak en büyük yeteneğiniz kırık kalpleri onarmaktır.
       \n
        Aile ve çocuklar sizin için çok önemlidir. Bu nedenle hayatınızda aile kurmak ve çocuk yetiştirmekle ilgili önemli derslerle karşılaşmak durumunda kalabilirsiniz. Ebeveynlikle ilgili olarak başka hiç bir rakam 6'lar kadar içten gelen doğal bir anlayışa sahip değildir. Ancak aile içinde dediğim dedik tutumunuzdan vazgeçmeli, başkalarının hayatına müdahale hakkınız olmadığını kabul etmelisiniz.
       \n
        Son derece verici bir doğanız var. Bu nedenle kendinizi ihmal etmemeye dikkat etmelisiniz çünkü kader sayısı 6 olanlar kendilerini başkaları için feda etmeye çok yatkındırlar. Kötümserlikten kaçınmalısınız. Başkalarının hayatlarına denge ve uyum getirirken kendi hayatınıza da aynı şeyi yapmakla sorumlu olduğunuzu unutmayın. İçsel dengenizi kurma yolunun başkalarına yardıma gönüllü olmaktan geçtiğini anladığınızda, başarının anahtarını da elinize almış olacaksınız.
       \n
        """,
        
        
        7: """
        Kader sayınız 7 ise, bu hayata bir taraftan ruhsal dünyanızla temas halinde olurken diğer yandan insanlarla sıcak ilişkiler kurmak için gelmiş bulunmaktasınız.
        \n
        7'ler mahremiyetlerine çok düşkündürler. Kalabalık içinde görünmez olmayı yeğlediklerinden çok iyi birer araştırmacı hatta dedektif olabilirler. Sır saklama konusunda onlara sonuna kadar güvenebiliriz. Gözlem ve analiz yetenekleri ise araştırma ve bilim alanlarında çok başarılı olmalarını sağlar.
       \n
        Siz bu dünyanın "düşünür"lerisiniz. İster doğa bilimleri olsun, ister din ve gizli öğretiler, gerçeğe ulaşmak adına her türlü bilgiyi sorgularsınız. Adeta bir filozof gibisiniz. Ancak zeki ve analitik doğanız nedeniyle zihne gereğinden fazla itimat etme ve duygulara fazla itibar etmeme eğiliminiz var. Oysa bu yaşamda zihin ve ruh dengesini sağlamak için bulunmaktasınız.
       \n
        Zaman zaman fazlasıyla şüpheci olabiliyorsunuz. Böyle durumlarda zihniniz yerine kalbinizin sesini dinlerseniz çok daha sağlıklı sonuçlara varırsınız.
       \n
        7'ler dışarıdan bakıldıklarında soğuk ve mesafeli görülebilirler çünkü konu duyguları oldu mu onları rahatlıkla ifade etmekte zorlanırlar. Ancak hayat amacınız bilgiyi paylaşmayı içerdiğinden başarınızın anahtarı zihinsel mağaranızdan çıkıp insan içine karışarak hayatınızdaki neşe enerjisini artırmakta yatmaktadır. Bu münzevilik eğiliminizi dengelemezseniz kendinizi yalnızlıktan şikayet ederken bulabilirsiniz.
       \n
       İronik bir şekilde bazı 7'ler yalnız kalma korkusuyla kendi içlerine dönmekten ve ruhsal yönleriyle temas kurmaktan kaçınırlar. Böyle yaptıklarında terk edilecekleri korkusunu duyarlar. Oysa bu korkuları yersizdir. En büyük zenginliği ruhsal yönlerini kabul edip onu geliştirdiklerinde ve bunu insanlarla paylaştıklarında yaşayacaklarını anlamalıdırlar. Şayet duygularınızı ifade etmekte çok fazla zorlanıyorsanız, onları yazarak ifade etmeyi deneyebilirsiniz, yeter ki ne kendinizle ne de insanlarla iletişiminizi kopartın.
        """, 
        
        8: """
        Kader sayınız 8 ise, bu hayata otoritenizi ve parayı doğru bir şekilde kullanmak için gelmiş bulunmaktasınız.
        \n
        8'ler iş veya diğer güç içeren pozisyonlarda dikkate değer bir başarı sağlama konusunda oldukça yüksek potansiyellere sahiptir. Yöneticilik becerileri çok gelişmiştir ve harika birer bankacı, borsacı, muhasebeci ve işletmeci olurlar. Tuttuklarını koparma konusunda son derece beceriklidirler.
          \n
        Siz bu dünyanın "simyacı"larındansınız. Para size kolayca akar ve onu nasıl yöneteceğinizi içsel olarak bilirsiniz. Koyduğunuz hedeflere sebatkar bir çalışmayla teker teker ulaşırsınız. Bu da otoritenizi güçlendirir ve takdir edilirsiniz. Ancak fazla hırslanmamaya dikkat edin çünkü daha fazla para kazanmak için ailenizi, arkadaşlarınızı ve sosyal hayatınızı ihmal etme eğilimindesiniz.
       \n
       Maddi konulardaki isabetli öngörüleriniz sizi insanları tahlil etme konusunda da iyi bir yorumcu yapar. Kolay kanmazsınız.
       \n
       Gücü sevdiğiniz kadar güçlü kişiliği de sevmektesiniz. Ancak güce tapma noktasına gelirseniz yargı yeteneğinizi kaybedeceğinizi, bunun da size maddi manevi büyük kayıplar yaşatacağını unutmayın. Sonuca varmanızı sağlayan şey hırstan arınmış vizyonunuzdur. Onu kaybederseniz kazandıklarınız da ellerinizin arasından kayar, üstelik ilişkileriniz de derin yaralar alır.
\n
       Maddi zaaflarınız nedeniyle yanlış arkadaşlıklar kurmama konusunda dikkatli olmalısınız. Ayrıca amacınızın karşısında gördüğünüz insanlara karşı gücünüzü duygusuzca kullanmaktan kaçınmalısınız. Hayat amacınızı para kazanma olarak değil, parayı ve gücü doğru şekilde yönetmek olarak gördüğünüz takdirde daima başarılı olacaksınız. Unutmayın; vermeden alamazsınız.
       
        """,
        
        9: """ 
        
        Kader sayınız 9 ise, bu hayata başkalarına yardım etmek ve sanatçı yönünüzü kullanmak için gelmiş bulunmaktasınız.
        \n
        Siz bu dünyanın "yardımsever"lerindensiniz. Harika birer öğretmen, danışman, din adamı, doktor, hukukçu ve sanatçısınız. Genellikle kariyer yapmak 9'ların listelerinin başında yer almaz, bu nedenle iş hayatına dair özel bir hırsları yoktur. Onlar daha çok insan doğasıyla ilgilidirler.
        \n
        Şefkatli, nazik ve ilgili doğanız insanların sizi Büyük Ablalaları ya da Büyük Ağabeyleri olarak görmelerine neden olur. Gönülden verirsiniz ve herkesin problemini çözmeye uğraşırsınız. Dostluk, sevgi ve aşk sizin için kariyerinizden bile büyük önem taşır. İnsanlarla yakın olarak çalıştığınız her işte başarılı olursunuz.         
        \n
        9'lar aynı zamanda son derece sanatsal yeteneklerle donanmıştır ancak maalesef bu yeteneklerini genellikle kullanmazlar. Oysa ki en başarılı edebiyatçı ve sanatçıların 9 kader sayısına sahip olduklarını görürüz. Bu yönlerini yaşamlarının daha geç dönemlerinde ifade etmeleri sık rastlanan bir durumdur.
        \n
        Kader sayınız 9 ise, hayırsever davranışlarla büyüyüp geliştiğinizi hissedersiniz. Değişim için gerekli olan en değerli şeyin bilgiyi hayata geçirmek olduğuna inanırsınız. Dünyayı güzelleştirmek ve daha iyi bir hale getirmeyi, insanları desteklemeyi kişisel hırslarınızın üzerinde tutarsınız. Gerçek bir dostsunuz. Oldukça da romantiksiniz.
        \n
        Bencillik etme ve kendine odaklı yaşama eğilimlerinize dikkat etmeniz gerekmektedir. Başarınızın anahtarını hislerinize kulak vermekte ve başkalarının ihtiyaçlarına karşı ilgili ve hassas davranmakta bulacaksınız. Bazen sert, uzak ve kibirli bir havanız olabilir. İnsanlar sizin yüksek ideallerinize uymadığı zaman hayal kırıklığına uğrarsınız. Oysa ki herkes aynı güç ve bilgi donanımına sahip değildir. İnsanları olduğu gibi kabul edip, onlara kendi bakış açılarından bakabilirseniz daha doyum verici ilişkiler kurduğunuzu göreceksiniz, bu da sizi mutlu edecek. Hayatın küçük detaylarının sizi fazlaca etkilemesine izin vermeyin.
    
        """,
        
        11: """ 
        
        Kader sayınız 11 ise, bu hayata ruhsal yönünüzü ve sezgilerinizi kullanmak için gelmiş bulunmaktasınız.
         \n
        Siz bu dünyanın "ruhsal rehber"lerindensiniz. Ruhsal yönünüz çok gelişmiştir. Güçlü ve doğru sezgileriniz insanların üzerinde dönüştürücü bir etki yaratır. Pozitif ve ilham verici enerjinizle ortamı aydınlatır, bu ruh halinizi başkalarına da bulaştırırsınız. İnsanlara ilham veren ve yol gösteren bu özelliğiniz sizi harika bir öğretmen, sosyal yardım uzmanı, filozof ve danışman yapar.
 \n
        11'lerin bilinç üstü oldukça gelişmiştir. Son derece sezgiseldirler, gizli öğretiler, dini veya doğaüstü olaylar çok ilgililerini çeker. Çoğu doğuştan medyumdur ve hayatlarının bir döneminde din adamı, astrolog, kanal, Reiki hocası, şifacı veya metafizikçi olurlar. Hayatlarının bu döneminin başlangıcı büyük bir değişim sonrası; örneğin muazzam derecede başarılı bir dönemden sonra beklenmedik sert ve dramatik bir düşüş yaşamaları sonucu gerçekleşir.
\n
        Öyle ya da böyle, bir şekilde sezgilerinizi ve psişik güçlerinizi doğru kullanmayı öğrenmek durumunda kalacaksınız. Gerçeği arayan yanınıza güvenirseniz, ister kalabalık ortamda olun, ister yalnız, karmaşa içinde dahi iç sesinizi duyabilirsiniz. Bu sese güvenin, sizi yanıltmayacaktır.
            \n    
        Kendinize ve başkalarına ulaşılması imkansız görünen hedefler koyma eğilimindesiniz. Bu konuda daha esnek olmalı, kendinizin ve diğerlerinin olumlu yönlerine odaklanmalısınız.  
        \n
        Çok fazla bilgiye sahip olmanızın getirdiği gerginlik zaten hassas olan sinir sisteminizi kolaylıkla bozar. Böyle anlarda kavgacılık ve üstünlük kurma eğiliminize dikkat etmelisiniz. Başarınızın anahtarını alçakgönüllülükte ve psişik güçlerinizi bütünün hayrına kullandığınızda bulacaksınız. Enerjinizi ve sinir sisteminizi dengede tutmak için yoga ve meditasyondan faydalanmak sizin için önemli olduğu kadar zorunludur da.
        
        """,
        
        22: 
            """
            Kader sayınız 22 ise, bu hayata içinizdeki muazzam gücü kullanarak dünyayı değiştirmek için gelmiş bulunmaktasınız.
            \n
            Kaderinizde ister politika, ister hukuk, tıp ya da eğlence sektörü olsun, herhangi bir alanda lider olmak var. Çocukken bile yaşlarından daha olgun olan 22'ler içsel olarak nereye yönelmeleri gerektiğini bilirler. Yaşlarının üzerinde bir bilgeliğe ve yeteneğe sahiptirler.
            \n
            Siz bu dünyanın "büyük inşacı"larındansınız. Dünyevi alanda büyük değişimleri tezahür ettirebilme gücüne sahipsiniz. Bunu da ister sosyal ister finansal anlamda olsun, bir çeşit imparatorluk kurarak gerçekleştirirsiniz. Güç, hayatınızın her zaman merkezinde olacaktır.
            \n
            22'ler dengeli, amacına bağlı ve pratik kişilerdir. Onları doğru yargılarda bulunmaya iten ve pratik çözümler üreten içsel bir pusulaları var gibidir. Düşünce gücünün farkındadırlar ve negatif düşüncelerin negatif, pozitif düşüncelerin pozitif sonuçlar yaratacağını bilirler. Onlar gerçek bir tezahür üstadıdır. Yaşamları boyunca daima ilgi odağıdırlar ve çekici bir hayat sürdürürler.
               \n         
            22'ler için en büyük tuzak, gördükleri sürekli ilgiden ötürü şımarmaları ve kendi güçlerinin büyüsüne kapılmalarıdır. Bu onları hayat amaçlarından uzaklaştırır, saldırgan ve yön duygusundan yoksun bir hale sokar. Başarıyı kanıksama hatasına düşerlerse yolunda gitmeyen ufak bir şeyi dahi kötü talih olarak yorumlama eğilimi gösterirler. Bu nedenle talihlerini takdir etme duygusunu geliştirmelidirler.
            \n   
            Odağınızı kendi gücünüz yerine bütünün hayrına yönlendirdiğiniz takdirde daima başarılı olursunuz. Unutmayın ki esas amacınız dünyayı ve insanlığı geliştirecek sistemler ve yapılar kurmaktır. Kendinize odaklandığınızda hem bu amaçtan hem de etrafınızdakilerden uzaklaşırsınız. Ayrıca sürekli geleceği düşünmekten kaçının ve anı kaçırmamaya çalışın. İnsanlık hayrına çalışmak gücünüze daima güç katacaktır.
           """
}


def get_original(weight):
    
    return q.get(weight)

    

def translate(weight):
    
    original_text = get_original(weight)
    
    translated = GoogleTranslator(source='auto', target='en').translate(original_text)
    
    return (original_text, translated)
    
    # pip install deep-translator

def process_name(name):
    
    if name.isalnum():
        return "Error: please provide alphabets only!", ""
    
    alphabet = {
        'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7,  'h' : 8, 'i' : 9, 
        'j' : 1, 'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7,  'q' : 8, 'r' : 9, 
        's' : 1, 't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6, 'y' : 7,  'z' : 8
    }
    
    
    name = name.lower().replace(" ", "").replace('.', '')
    
    weight = 0
    for char in name:
        weight = weight + alphabet.get(char)
        
    
    if weight == 11 or weight == 22 or weight < 10:
        return weight 
    
    else:
        str_weight = str(weight)
        print(str_weight)
        sum_weight = weight
        while len(str_weight) >= 2 and (sum_weight != 11 or sum_weight!=22): 
            sum_weight = 0
            for i in str_weight:
                print('-' * 10)
                sum_weight = sum_weight + int(i)
                
                time_duration = 1.5
                time.sleep(time_duration)
                print('weight >> ', sum_weight)
            
            str_weight = str(sum_weight)
            print('-->',str_weight)
            
    
    return sum_weight