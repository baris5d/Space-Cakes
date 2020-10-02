var n = 2;
var t = 60;
var d = 2;

var balls = [
 {
  x: 10,
  v: 1
 },
 {
  x: 95,
  v: -1
 }
];

for(i = 1; i < 60; i++) { // her saniye için döngümüz

    for(b = 0; b < n; b++) { // bu her topun hareketini kontrol etmek için 

 // hareketini ivme kadar arttırıyoruz
 balls[b].x += balls[b].v;
 
 if(balls[b].x >= 100 || balls[b].x <= 0) {
    // Cebe girdiyse
     if(b == d - 1) {
      // Eğer top istenilen index’se bunun konumunu döndür direkt
         console.log(balls[b].x);
    } else {
      // değilse balls arrayinden b ivmesini 0 yap hareket edemesin
       balls[b].v = 0; 
      // hatta alanda işlem görmemesi için x’i haritanın dışına çıkarabiliriz
     balls[b].x = -10;
    
    }

 }

 

 if(balls[b+1] !== undefined) { // Bi üst indexte (ileride) top var mı kontrol et
   if(balls[b].x >= balls[b+1].x) { // Topla çarpışmış mıyız kontrol et 
      
        balls[b].v = 0 - balls[b].v;
        balls[b+1].v = 0 - balls[b+1].v;
      // Şu anki topu ve diğer topun ivmelerini tersine çevir
   }
 }

 }

}

// Süre bitti istenilen indexin konumunu döndür
console.log(balls[d-1].x);