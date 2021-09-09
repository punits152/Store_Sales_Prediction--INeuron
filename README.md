# Store_Sales_Prediction--INeuron
Data is available at the store and item level. A predictive model is to be prepared to predict the sales. The deployment using flask is also done for the best predictive model

## Data Description

## Architecture
<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=5,IE=9" ><![endif]-->
<!DOCTYPE html>
<html>
<head>
<title>Architecture.html</title>
<meta charset="utf-8"/>
</head>
<body>
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;Electron\&quot; modified=\&quot;2021-09-09T19:56:14.506Z\&quot; agent=\&quot;5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/15.1.3 Chrome/89.0.4389.128 Electron/12.1.0 Safari/537.36\&quot; etag=\&quot;s15NGgE1W7nNPm4w2oEj\&quot; version=\&quot;15.1.3\&quot; type=\&quot;device\&quot;&gt;&lt;diagram name=\&quot;Page-1\&quot; id=\&quot;97916047-d0de-89f5-080d-49f4d83e522f\&quot;&gt;5Vttk6I4EP41ftwrCPLixxl1Zq/q9m5u3drdr1EiZicSKgQd79dfgESBZBysUUaX+TAFTchL9/N0dzo4cMbrl0cGk9UXGiIyAFb4MnAmAwACF4j/uWBXCmzfGf7hlrKI4VBKD4IZ/g9JoSWlGQ5RWmvIKSUcJ3XhgsYxWvCaDDJGt/VmS0rqoyYwQppgtoBESdV8c/kPHPKVlNve6PDgM8LRSg4eAL98MIeL54jRLJYjxjRG5ZM1VN3IVaYrGNJtReRMB86YUcrLq/XLGJFctUpn5XsPrzzdL4WhmLd54fnL0IY/rXW0Cf9lq10C5tPvnwLZzQaSTGpDzpbvlHpQKLQlbynjKxrRGJLpQXpfKADl41ji7tDmL0oTIbSF8BfifCdNDzNOhWjF10Q+1dci55XSjC3kPOTMOGQRkq2cUpTPsPKaXP8jomvE2U40YIhAjjd1FEAJm2jf7qA9cSEVaFYm0NQ2E/Pimu4OmsmXucSEjCmhrHjo2JbvjET39yln9BmpJwWGhFDhJX8zYjDEQjmNNksac2UaW95XBngo/lS7Uvn28Ji+N4hx9HJUl+rpSOJa8v6TI++3FQINpWxV4Y5nvV/9Riy77u1g2dGxbH8YmB1NbxPIoZD8GUco5ZjGPcK147XAtRdcBte+ZomxgB1isGdGsIEPalYYuq4K0hU7AKtL/+LpTv8j/EvdLG2cjW3wNmYPOvooF2S/6oPGBMEYx1GP0O+2ckEXgr4hGnxFUSbsTYs5DoBX6FcsFYqsF1jTeEkF1Nb5eoE1wRuc9sxZWaO6s/LsTp0VGGoW+2e5xIL9wKJL8a9mvydK8GLXZ/P4Vrfm0dPSvXnGdJ0QDOMF6rVBRt0axHuDLxUXV3Nu/bVQEHRrIT0Prllob56mc5tlSUL7tQ1vmmrkd2oq19JMpWm/mhQjMqfbaj5cCMSDfMl4AcneDqoQlysKxeFdXugTt3NCF8+l6AETc1LcNKWwAXCGQ3fSutRkyJhVmH0zOZaWaexgbM9kF9tkl73QZBg53hPFRb5lHgwcBlN9lMuTr4FKmbDRk/36vFVXpVa0rgqo7PXQDj0nlh9vBD1DA3rc96HHyOpLocc/H3r0rs6InhM35DeCHteAHu996DGG70uhJzgfevSuzogefaP7O6DHM6DHfx96jOn5pdAzOh969K7Ohx5j/czXdxZHIfWRJxDmAqABPeaVtg1nZ68UHp13RfGPQkVF2dCShUShJaEUhkK86NMGoXmeYbuGYqLfZR3dP9HxXh9L/JYs8T6snn503hXFPzEkNFDy5IHA9Lle/rhLEiJCW99OnxpH256BMZ2ebHs3dLJtRl7QljHWdTEm0BSvPoC6zzAJ+3Uu5asN1xFeXOpk3BxJTtwAXh8vRi15oYB4LbwYaYqXWdY3BuN0Sdm6b0GjSY5Ovxsx+1L9XPC22KE083bUsK+KHZ5eE1dR41vW828ZjDGj01xKD+k3xgr1ifSbMaNt2acjVui1fsWKGdz0ixWOQuG1sMK/+VjROpNqW0rviBV6JnWfyY2F9ZVmHKX5sPmXVh4R67qfM3EV5Vc/0Dz/XUKqGWq7whzNElgobMtgUldynVY1pjShfpQSrxatFb9eIewZ+NPcoRuLWp1u0f1bDyu+4djJ3PC6woqv10aeyiKvaf/x+1OjmXAZqdFpbAlO/ETk+qjRtt7rn73eW7x6xxjcVRok+flVWum5cRAWOF4NAsC3GkYsezzv2ZdeXFZpnXUgZKqHseJcZjz73kOuNmsGZq52WlHT05Hp35Memsa16m4UmMo5wOBG3dNNI24PPwMt+Xj4qa0z/R8=&lt;/diagram&gt;&lt;/mxfile&gt;&quot;,&quot;toolbar&quot;:&quot;pages zoom layers lightbox&quot;,&quot;page&quot;:0}"></div>
<script type="text/javascript" src="https://app.diagrams.net/js/viewer-static.min.js"></script>
</body>
</html>
![](info/Architecture.html "Architecture")
