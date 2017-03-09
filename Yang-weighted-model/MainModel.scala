import scala.io.Source

object MainModel {
  val usage = """
    Usage: mmlaln [Number of input sentences] [Target grammar code (French=584, English=611, German=2253, Japanese=3856)]
  """
  def main(args: Array[String]): Unit = {
    if (args.length != 2){
      println(usage)
      return
    }

    println("Hello, world!")
    // Read in language file
    val colagFile = "../EngFrJapGerm.txt"
    
    // Choose target language and number of input sentences to parse
    val targetSentences = List()
    for (line <- Source.fromFile(colagFile).getLines.filter(line => line(0) != args(1)).split('\t')) {
      println(line)
    }
  }
}
