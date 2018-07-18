import {
  wxRequest
} from '@/utils/wxRequest';

const host = 'https://h878.cn';

//  注册  UStelphone   USpassword  UScode  USinvatecode
const register = params => wxRequest(params, host+'/group/meal/user/register');
// 用户协议
const getText = () => wxRequest('', host+'/group/meal/other/disclaimer');
// 获取验证码
const getValidate = (params) => wxRequest(params, host+'/group/meal/user/get_inforcode');
//  登录  UStelphone  USpassword
const login = params => wxRequest(params, host+'/group/meal/user/login');
//  更新基础信息
const updateInfo = params => wxRequest(params, host+`/group/meal/user/update_info?token=${params.token}`);
//  更新密码
const updatePwd = params => wxRequest(params, host+'/group/meal/user/update_pwd');
//  获取个人基础信息  GET
const allInfo = params => wxRequest(params, host+`/group/meal/user/all_info?token=${params.token}`);
//  填写第一份个人资料
const updateFirstUser = params => wxRequest(params, host+`/group/meal/user/update_first_user?token=${params.token}`);
//  忘记密码
const forgetPwd = params => wxRequest(params, host+'/group/meal/user/forget_pwd');
//  获取验证码
const getInforcode = params => wxRequest(params, host+'/group/meal/user/get_inforcode');

//  创建餐品
const newMeal = params => wxRequest(params, host+'/group/meal/meal/new_meal');
//  更新餐品
const updateMeal = params => wxRequest(params, host+'/group/meal/meal/update_meal');
//  获取某食堂餐品列表 GET
const mealList = params => wxRequest(params, host+`/group/meal/meal/meal_list?MSid=${params.MSid}&MEtag=${params.MEtag}`);
//  获取餐品详情  GET
const mealAbo = params => wxRequest(params, host+`/group/meal/meal/meal_abo?MEid=${params.MEid}`);


//  创建食堂
const newMess = params => wxRequest(params, host+`/group/meal/mess/new_mess`);
//  根据城市获取食堂  GET
const getMessByCity = params => wxRequest(params, host+`/group/meal/mess/get_mess_by_city?MScity=${params.MScity}`);
//  获取食堂详情  GET
const getMessAbo = params => wxRequest(params, host+`/group/meal/mess/get_mess_abo?MSid=${params.MSid}`);
//  获取已开放的城市  GET
const getAllCity = params => wxRequest(params, host+`/group/meal/mess/get_all_city`);


export default {
  register,
  getText,
  getValidate,
  login,
  updateInfo,
  updatePwd,
  allInfo,
  updateFirstUser,
  forgetPwd,
  getInforcode,
  newMeal,
  updateMeal,
  mealList,
  mealAbo,
  newMess,
  getMessByCity,
  getMessAbo,
  getAllCity

}
