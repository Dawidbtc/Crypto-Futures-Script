<h1>Crypto Futures Script</h1>
<h3> This is a script that can be used to calculate current yield from capturing futures premium. This can be done by selling futures and buying spot. Inversely if yield is negative, the yield can be captured by selling spot and buying futures. </h3>
<br><h3>Price feeds are obtained via FTX API. Perp market is used instead of spot market for spot because FTX has been known to have lacking liquidity on spot markets for some markets so perp markets will prevent deviations if calculating premium on illiquid coins. Perpetual markets are usually very close to spot market anyway. The most farthest out futures expiry is used for yield calculations.</h3>
<br>
<h3>Current coins supported:
<ul>
<li>Bitcoin</li>
<li>Ethereum</li>
<li>Solana</li>
<li>BNB</li>
<li>Ripple</li>
<li>Dogecoin</li>

