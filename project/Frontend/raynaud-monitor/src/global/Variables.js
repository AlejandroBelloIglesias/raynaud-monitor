

// check if mode production or development
export let BASE_URI = ""
switch (process.env.NODE_ENV) {
    case 'production':
        BASE_URI = "http://95.22.240.188:5000" // npm run probuild y npm run proserve
        break;
    case 'test':
        BASE_URI = "http://192.168.1.3:5000"  // npm run testbuild y npm run testserve
        break;
    default:
        BASE_URI = "http://localhost:5000" // npm run devbuild y npm run devserve
        break;
}
//http://95.22.240.188 //Mi servidor (IP Pública)
//http://192.168.1.3 //Mi servidor (Desde LAN)
//http://localhost:8000 //Local

export const VERSION = "1.0.0-alpha"