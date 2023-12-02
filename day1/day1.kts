import khoury.*;

fun main(){
  val input = fileReadAsList("day1input.txt")
  var sum = 0;

  for(line in input){
    var left = '-'
    var right = '-'
    
    for(char in line){
      if(Character.isDigit(char)){
        if(left =='-'){
          left = char
        }
        right = char
      }
    }
    val ans  =  ""+left+right
    sum += Integer.parseInt(ans)
  }
  println(sum);
}
main()