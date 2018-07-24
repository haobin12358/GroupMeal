import wepy from 'wepy';
import tip from './tip';

const wxRequest = async(params = {}, url) => {
  tip.loading();
  wepy.showNavigationBarLoading()
  let data = params.query || {};
  // data.time = TIMESTAMP;
  let res = await wepy.request({
    url: url,
    method: params.method || 'GET',
    data: data,
    header: { 'Content-Type': 'application/json' },
  });
  tip.loaded();
  wepy.hideNavigationBarLoading()
  return res;
};


module.exports = {
  wxRequest
}
