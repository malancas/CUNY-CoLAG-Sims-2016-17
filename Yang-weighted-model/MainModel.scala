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
    // Read target language sentences from EngFrJapGerm.txt
    val targetSentences = io.Source.fromFile("../EngFrJapGerm.txt").getLines.map(x => x.split('\t')).filter(line =>line(0) == args(1)).toArray
    println(targetSentences.deep.mkString("\n"))
  }
}
