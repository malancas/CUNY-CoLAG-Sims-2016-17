package modelfunctions

class ModelFunctions {
  def sayHello(): Unit = {
    println("Hello!")
  }

  def updateGrammarGo(w: Double, weights: List[Double], newGrammar: List[Char]): List[Char] = {
    weights match {
      case h :: t =>
        if (h == w) updateGrammarGo(w, t, newGrammar :+ '1')
        else updateGrammarGo(w, t, newGrammar :+ '0')

      case Nil => newGrammar
    }
  }

  def updateGrammar(w: Double, weights: List[Double]): List[Char] = {
    if (w == 0.5){
      val r = new scala.util.Random
      List.fill(13)((48 + r.nextInt((1 - 0) + 1)).toChar)
    }
    else updateGrammarGo(w, weights, List.empty)
   }

  def reward(weight: Double, w: Double): Double = {
    (weight + w * (1-weight))
  }

  def punish(weight: Double, w: Double): Double = {
    ((1 - w) * weight) 
  }

  def updateWeights(w: Double, weights: List[Double], grammar: List[Char], parsed: Boolean, newWeights: List[Double]): List[Double] = {    
    weights match {
      case h :: t =>
        // Reward
        if ((parsed && grammar.head == '1') || (!parsed && grammar.head == '0')){
          updateWeights(w, t, grammar.tail, parsed, newWeights :+ reward(h, w))
        }
        // Penalty
        else if ((parsed && grammar.head == '0') || (!parsed && grammar.head == '1')){ 
          updateWeights(w, t, grammar.tail, parsed, newWeights :+ punish(h, (1 - w)))
        }
        else {
          println("Should never reach here")
          List()
        }
      case nil => newWeights
    }
  }

  // Each sentence is parsed by the grammar
  def parseSentences(i: Int, max: Int, targetGrammar: List[Char], grammar: List[Char], weights: List[Double], w: Double): List[Char] = {
    if (i == max) grammar
    else {
      //Step 1: Update grammar
      val newGrammar = updateGrammar(w, weights)
      val wIndex = newGrammar.indexOf('1')

      // Step 2: Parse sentence
      // If targetGrammar and newGrammar are equal, the
      // sentence has been successfully parsed
      val newWeights = if (targetGrammar == newGrammar) updateWeights(w, weights, newGrammar, true, List.empty) else updateWeights(w, weights, newGrammar, false, List.empty)
      val wNew = if (wIndex < 0) (1 - newWeights(0)) else newWeights(wIndex)

      parseSentences(i + 1, max, targetGrammar, newGrammar, newWeights, wNew)
    }
  }
}
/*

  def linearRewardSchemeGo(i: Int, targetIndex: Int, weights: List[Double], grammar: List[Double], newWeights: List[Double], weightParameter: Double): List[Double] =
    weights match {
      case h :: t =>
        if (i == targetIndex) linearRewardSchemeGo(i+1, targetIndex, weights.tail, grammar.tail, newWeights :+ (h + weightParameter * (1 - h)))
        else linearRewardSchemeGo(i+1, targetIndex, weights.tail, grammar.tail, newWeights :+ ((1 - weight) * h))
    }

  def updateWeights(weights: List[Double], grammar: List[Int], parsed: Boolean, newWeights: List[Double]): List[Double] =
    weights match {
      case h :: t =>
        // Reward
        if ((parsed && grammar.head == 1) || (!parsed && grammar.head == 0)){
          updateWeights(t, grammar.tail, parsed, newWeights :+ reward(h, grammar.head))
        }
        // Penalty
        else if ((parsed && grammar.head == 0) || (!parsed && grammar.head == 1)){ updateWeights(t, grammar.tail, parsed, newWeights :+ punish(h, grammar))
        }
        else {
          println("Should never reach here")
          List()
        }
      case nil => newWeights
    }

  // Assumes that only each weight is only updated once, when it's corresponding parameter is reached
  def scenario1(grammar: Seq[Double], weights: List[Double]): Seq[Double] = {
    updateWeights(weights, grammar, parsed, List[])
  }

  // Implementing LRP-scheme: https://books.google.com/books?id=-zdWJ9Adp1wC&pg=PA110&lpg=PA110&dq=linear+reward+penalty+scheme+bush&source=bl&ots=u6IsuDpd5y&sig=CVtmdd6SYgtni3nQj2yDx-phZoI&hl=en&sa=X&ved=0ahUKEwiO8sHb0MrSAhVEzIMKHRPCDZMQ6AEIKzAD#v=onepage&q=linear%20reward%20penalty%20scheme%20bush&f=false
 */   
